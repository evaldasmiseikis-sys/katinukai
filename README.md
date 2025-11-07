# 🔍 AI Image Analyzer

A modern Streamlit application that uses Ollama models to analyze uploaded images with AI. Features a beautiful, responsive UI with structured output parsing and comprehensive image insights.

## ✨ Features

- 🎨 **Modern UI Design** - Clean, gradient headers and card-based layout
- 📊 **Structured Analysis** - Parses model responses into organized sections
- 🔍 **Detailed Insights** - Descriptions, key observations, detected objects, and tags
- 📈 **Confidence Scoring** - AI confidence levels for analysis reliability
- 📷 **Image Metadata** - File details, dimensions, and format information
- 🏷️ **Smart Tagging** - Automatic tag generation with visual tag display
- 📋 **Multiple Views** - Summary, detailed analysis, and raw data tabs
- ⚙️ **Customizable Prompts** - Modify analysis focus and instructions
- 🚀 **Real-time Processing** - Live progress indicators and error handling

## 📁 Files

- `app.py` — Enhanced Streamlit application with modern UI and structured parsing
- `requirements.txt` — Python dependencies (streamlit, ollama, Pillow)
- `model.txt` — Model configuration (reads Ollama model name)
- `app-promt.txt` — Default system prompt for analysis

## 🚀 Quick Start (Windows PowerShell)

1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Ensure Ollama is running locally (if you use local Ollama):

```powershell
ollama serve
```

4. Run the Streamlit app:

```powershell
streamlit run app.py
```

## 🎯 Usage Tips

- **Model Configuration**: Edit `model.txt` to change the Ollama model (default: `gemma3:4b`)
- **Custom Prompts**: Modify `app-promt.txt` or use the in-app editor to customize analysis focus
- **Image Support**: Upload JPG/JPEG files up to 10MB for best performance
- **Structured Output**: The app intelligently parses AI responses into organized sections
- **Multiple Views**: Switch between Summary, Detailed Analysis, and Raw Data tabs

## 🛠️ Troubleshooting

### Common Issues

- **Import Errors**: Run `pip install -r requirements.txt` to install dependencies
- **Ollama Connection**: Ensure Ollama is running with `ollama serve`
- **Model Issues**: Make sure `gemma3:4b` is available with `ollama pull gemma3:4b`
- **Upload Problems**: Check file format (JPG/JPEG only) and size limits
- **Analysis Errors**: Restart Ollama service if the model fails to respond

### Model Requirements

The app uses `gemma3:4b` which is a **multimodal vision model** capable of analyzing images. Make sure you have it installed:

```powershell
# Install the required model
ollama pull gemma3:4b

# Verify it's available
ollama list
```

The model name is read from `model.txt` - you can change it there if needed, but `gemma3:4b` is recommended for its vision capabilities.

## 🎨 UI Features

- **Responsive Design**: Works on desktop and tablet screens
- **Visual Hierarchy**: Color-coded sections and intuitive navigation
- **Progress Indicators**: Real-time feedback during analysis
- **Error Handling**: Helpful error messages and recovery suggestions
- **Metadata Display**: Comprehensive image information in sidebar
