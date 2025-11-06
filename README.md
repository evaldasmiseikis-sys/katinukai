# katinukai
individuali užduotis

## File Upload and Analysis Application

A web application that allows users to upload files and analyzes them to extract useful information and metadata.

### Features

- **File Upload Interface**: Modern, user-friendly drag-and-drop interface
- **Multiple File Type Support**: Handles TXT, PDF, Images (PNG, JPG, JPEG, GIF), CSV, JSON, XML, DOC, DOCX
- **Comprehensive Analysis**:
  - File metadata (size, type, extension)
  - Text file analysis (character count, word count, line count, content preview)
  - Image analysis (dimensions, format, color mode)
  - File size in human-readable format
- **Security**: File type validation and secure filename handling
- **Responsive Design**: Works on desktop and mobile devices

### Installation

1. Clone the repository:
```bash
git clone https://github.com/evaldasmiseikis-sys/katinukai.git
cd katinukai
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. (Optional) Set environment variables:
```bash
export SECRET_KEY='your-secure-random-secret-key'
```
Note: If not set, a random key will be generated automatically.

2. Start the application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload a file:
   - Click on the upload area or drag and drop a file
   - Click "Analyze File" button
   - View the analysis results

### API Endpoints

#### `GET /`
Main page with file upload interface

#### `POST /upload`
Upload and analyze a file

**Request:**
- Content-Type: multipart/form-data
- Body: file (binary)

**Response:**
```json
{
    "success": true,
    "analysis": {
        "filename": "example.txt",
        "size_bytes": 1024,
        "size_human": "1.00 KB",
        "mime_type": "text/plain",
        "extension": "txt",
        "type": "text",
        "character_count": 1000,
        "line_count": 20,
        "word_count": 150,
        "preview": "First 500 characters..."
    }
}
```

#### `GET /health`
Health check endpoint

**Response:**
```json
{
    "status": "healthy"
}
```

### Configuration

You can modify the following settings in `app.py`:

- `MAX_CONTENT_LENGTH`: Maximum file size (default: 16MB)
- `UPLOAD_FOLDER`: Directory to store uploaded files (default: 'uploads')
- `ALLOWED_EXTENSIONS`: Set of allowed file extensions

Environment variables:
- `SECRET_KEY`: Flask secret key for session management (auto-generated if not set)
- `FLASK_DEBUG`: Set to 'true' to enable debug mode (default: false for security)

### File Analysis Details

#### Text Files (TXT, CSV, JSON, XML)
- Character count
- Line count
- Word count
- Content preview (first 500 characters)

#### Images (PNG, JPG, JPEG, GIF)
- Dimensions (width x height)
- Image format
- Color mode (RGB, RGBA, etc.)
- Requires Pillow library

#### Other Files
- Basic metadata analysis (filename, size, type)

### Security Considerations

- Files are validated against allowed extensions
- Filenames are sanitized using `secure_filename()`
- Maximum file size limit enforced
- Secret key uses environment variable or generates random key
- Uploaded files are automatically deleted after analysis
- Consider adding authentication for production use
- Use a production WSGI server (like Gunicorn) for production deployment

### Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **File Handling**: Werkzeug
- **Image Processing**: Pillow (PIL)

### Development

To run in development mode with debug enabled:
```bash
export FLASK_DEBUG=true
python app.py
```

With debug mode enabled, the application will reload automatically when you make changes to the code.

**Note:** Debug mode should never be enabled in production as it can expose security vulnerabilities.

### License

This project is part of an individual assignment (individuali užduotis).

### Future Enhancements

- PDF content extraction and analysis
- Document word count for DOC/DOCX files
- CSV data preview and statistics
- JSON structure validation
- File format conversion
- Batch file upload
- Download analysis reports
- User authentication
- Database storage for analysis history
