# katinukai - File Upload and Analysis Application

A web application that allows users to upload files and automatically analyzes them according to their type and content.

## Features

- **File Upload Interface**: Simple and intuitive web interface for uploading files
- **Automatic File Analysis**: Analyzes uploaded files based on their type
- **Multiple File Type Support**: Handles text files, CSV, JSON, images, PDF, and more
- **Content Analysis**:
  - Text files: Line count, word count, character count, content preview
  - CSV files: Row and column counting, data preview
  - JSON files: Structure validation, key/element counting
  - All files: Type detection, size calculation, MIME type identification
- **Secure Handling**: File type validation and secure filename sanitization

## Supported File Types

- Text files: `.txt`
- Documents: `.pdf`, `.doc`, `.docx`
- Images: `.png`, `.jpg`, `.jpeg`, `.gif`
- Data files: `.csv`, `.json`, `.xml`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/evaldasmiseikis-sys/katinukai.git
cd katinukai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload a file using the web interface

4. View the analysis results

## Configuration

- Maximum file size: 16 MB (configurable in `app.py`)
- Upload directory: `uploads/` (automatically created)
- Allowed file extensions can be modified in `app.py`

## Security Considerations

⚠️ **Important**: This application is configured for development use:
- Debug mode is enabled by default
- The secret key is a development placeholder
- The app binds to all network interfaces (0.0.0.0)

**For production deployment:**
1. Set `debug=False` in `app.py`
2. Use a strong, randomly generated secret key from environment variables
3. Configure the host and port appropriately for your deployment
4. Use a production WSGI server (e.g., Gunicorn, uWSGI) instead of Flask's built-in server
5. Implement proper authentication and authorization if needed
6. Consider adding HTTPS/TLS support

## Project Structure

```
katinukai/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Upload page
│   ├── results.html   # Analysis results page
│   └── about.html     # About page
└── uploads/           # Uploaded files directory (created automatically)
```

## Requirements

- Python 3.7+
- Flask 3.0.0
- Werkzeug 3.0.1
- python-magic 0.4.27

## Development

The application runs in debug mode by default. For production deployment, set `debug=False` in `app.py` and configure a proper secret key.
