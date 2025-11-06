"""
File Upload and Analysis Application
A Flask web application that allows users to upload files and analyzes them.
"""

import os
import mimetypes
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'json', 'xml', 'doc', 'docx'}


def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def analyze_file(filepath, filename):
    """
    Analyze the uploaded file and return analysis results.
    
    Args:
        filepath: Path to the uploaded file
        filename: Original filename
    
    Returns:
        Dictionary containing analysis results
    """
    analysis = {
        'filename': filename,
        'upload_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'file_size': os.path.getsize(filepath),
        'file_size_readable': format_file_size(os.path.getsize(filepath)),
    }
    
    # Detect file type
    mime_type, _ = mimetypes.guess_type(filepath)
    analysis['mime_type'] = mime_type or 'Unknown'
    
    # Get file extension
    extension = filename.rsplit('.', 1)[1].lower() if '.' in filename else 'none'
    analysis['extension'] = extension
    
    # Analyze content based on file type
    if extension == 'txt' or mime_type and mime_type.startswith('text/'):
        analysis.update(analyze_text_file(filepath))
    elif extension in ['csv']:
        analysis.update(analyze_csv_file(filepath))
    elif extension in ['json']:
        analysis.update(analyze_json_file(filepath))
    elif extension in ['png', 'jpg', 'jpeg', 'gif']:
        analysis['content_type'] = 'Image file'
    elif extension in ['pdf']:
        analysis['content_type'] = 'PDF document'
    else:
        analysis['content_type'] = 'Binary or unknown file type'
    
    return analysis


def format_file_size(size_bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def analyze_text_file(filepath):
    """Analyze a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        words = content.split()
        
        return {
            'content_type': 'Text file',
            'line_count': len(lines),
            'word_count': len(words),
            'character_count': len(content),
            'preview': content[:500] if len(content) > 500 else content
        }
    except UnicodeDecodeError:
        return {
            'content_type': 'Text file (binary content)',
            'error': 'Unable to decode as text'
        }


def analyze_csv_file(filepath):
    """Analyze a CSV file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        row_count = len(lines)
        column_count = len(lines[0].split(',')) if lines else 0
        
        return {
            'content_type': 'CSV file',
            'row_count': row_count,
            'column_count': column_count,
            'preview': ''.join(lines[:10]) if len(lines) > 10 else ''.join(lines)
        }
    except Exception as e:
        return {
            'content_type': 'CSV file',
            'error': f'Error analyzing CSV: {str(e)}'
        }


def analyze_json_file(filepath):
    """Analyze a JSON file."""
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        result = {
            'content_type': 'JSON file',
            'valid_json': True,
        }
        
        if isinstance(data, dict):
            result['json_type'] = 'Object'
            result['key_count'] = len(data.keys())
        elif isinstance(data, list):
            result['json_type'] = 'Array'
            result['element_count'] = len(data)
        else:
            result['json_type'] = type(data).__name__
        
        result['preview'] = json.dumps(data, indent=2)[:500]
        
        return result
    except json.JSONDecodeError as e:
        return {
            'content_type': 'JSON file',
            'valid_json': False,
            'error': f'Invalid JSON: {str(e)}'
        }


@app.route('/')
def index():
    """Display the upload form."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and analysis."""
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Analyze the file
        analysis_results = analyze_file(filepath, filename)
        
        return render_template('results.html', analysis=analysis_results)
    else:
        flash('File type not allowed. Allowed types: ' + ', '.join(ALLOWED_EXTENSIONS), 'error')
        return redirect(url_for('index'))


@app.route('/about')
def about():
    """Display information about the application."""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
