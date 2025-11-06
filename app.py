"""
File Upload and Analysis Application

This Flask application allows users to upload files and performs various analyses on them.
"""

import os
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
import mimetypes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'json', 'xml', 'doc', 'docx'}

# Create uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def analyze_text_file(filepath):
    """Analyze text-based files."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return {
            'type': 'text',
            'character_count': len(content),
            'line_count': len(content.split('\n')),
            'word_count': len(content.split()),
            'preview': content[:500] if len(content) > 500 else content
        }
    except UnicodeDecodeError:
        return {
            'type': 'text',
            'error': 'Unable to decode file as text'
        }


def analyze_file(filepath, filename):
    """
    Analyze the uploaded file and return analysis results.
    
    Args:
        filepath: Full path to the uploaded file
        filename: Original filename
        
    Returns:
        dict: Analysis results including file metadata and content analysis
    """
    file_stats = os.stat(filepath)
    mime_type, _ = mimetypes.guess_type(filename)
    
    analysis = {
        'filename': filename,
        'size_bytes': file_stats.st_size,
        'size_human': format_bytes(file_stats.st_size),
        'mime_type': mime_type or 'unknown',
        'extension': filename.rsplit('.', 1)[1].lower() if '.' in filename else 'none'
    }
    
    # Perform content analysis based on file type
    if analysis['extension'] in ['txt', 'csv', 'json', 'xml']:
        content_analysis = analyze_text_file(filepath)
        analysis.update(content_analysis)
    elif analysis['extension'] in ['png', 'jpg', 'jpeg', 'gif']:
        try:
            from PIL import Image
            img = Image.open(filepath)
            analysis['type'] = 'image'
            analysis['dimensions'] = f"{img.width}x{img.height}"
            analysis['format'] = img.format
            analysis['mode'] = img.mode
        except ImportError:
            analysis['type'] = 'image'
            analysis['note'] = 'Install Pillow for detailed image analysis'
        except Exception as e:
            analysis['type'] = 'image'
            analysis['error'] = str(e)
    else:
        analysis['type'] = 'other'
        analysis['note'] = 'Basic analysis only - specialized analysis not available for this file type'
    
    return analysis


def format_bytes(bytes_size):
    """Format bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"


@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and analysis."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file
        file.save(filepath)
        
        # Analyze the file
        analysis_results = analyze_file(filepath, filename)
        
        # Optionally clean up the file after analysis
        # os.remove(filepath)
        
        return jsonify({
            'success': True,
            'analysis': analysis_results
        })
    
    return jsonify({'error': 'File upload failed'}), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
