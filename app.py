import io
import json
import base64
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🔍 AI Image Analyzer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

ROOT = Path(__file__).parent


def load_model_name():
    p = ROOT / "model.txt"
    if p.exists():
        return p.read_text(encoding="utf-8").strip()
    return "gemma3"


def load_app_prompt():
    p = ROOT / "app-promt.txt"
    if p.exists():
        return p.read_text(encoding="utf-8").strip()
    return "Analyze the uploaded image and provide a concise, structured analysis."


MODEL = load_model_name()
SYSTEM_PROMPT = load_app_prompt()


def parse_structured_response(text: str) -> Dict[str, Any]:
    """Try to extract structured data from model response."""
    result = {
        "description": "",
        "key_observations": [],
        "objects": [],
        "tags": [],
        "confidence": 0,
        "raw_text": text
    }
    
    # Try JSON parsing first
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            result.update(parsed)
            return result
        except:
            pass
    
    # Fallback: regex patterns for common structures
    desc_match = re.search(r'(?:description|summary)[:]\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if desc_match:
        result["description"] = desc_match.group(1).strip()
    
    # Extract lists (observations, objects, tags)
    obs_pattern = r'(?:observations?|findings?)[:]\s*(.+?)(?:\n\n|\n[A-Z]|$)'
    obs_match = re.search(obs_pattern, text, re.IGNORECASE | re.DOTALL)
    if obs_match:
        obs_text = obs_match.group(1)
        result["key_observations"] = [line.strip('- •').strip() 
                                    for line in obs_text.split('\n') 
                                    if line.strip() and not line.strip().isdigit()]
    
    # Extract confidence score
    conf_match = re.search(r'confidence[:]\s*(\d+)', text, re.IGNORECASE)
    if conf_match:
        result["confidence"] = int(conf_match.group(1))
    
    return result


def call_ollama_analysis(image_bytes: bytes, model: str, prompt: str) -> dict:
    """Call Ollama chat with an image. Returns parsed response or raises."""
    try:
        # Import lazily to keep app import light if ollama isn't installed
        from ollama import chat
        import base64

        # Enhanced prompt for structured output
        user_prompt = """Please analyze this image and provide a detailed response in this format:

DESCRIPTION: [Brief 1-2 sentence description of what you see]

KEY OBSERVATIONS:
- [Key observation 1]
- [Key observation 2] 
- [Key observation 3]

OBJECTS DETECTED: [List main objects/subjects]

SUGGESTED TAGS: [Relevant tags/keywords]

CONFIDENCE: [Score from 0-100 indicating analysis confidence]

ADDITIONAL NOTES: [Any other relevant details]"""

        # Convert image bytes to base64 string (Ollama expects this format)
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')

        # Prepare messages: system + user with base64 image
        messages = [
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": user_prompt,
                "images": [image_b64],  # Use 'images' array with base64 string
            },
        ]

        # Call Ollama synchronously with lower temperature for more consistent results
        response = chat(model=model, messages=messages, options={"temperature": 0.1, "seed": 42})

        # Try to extract content in various ways
        content = None
        try:
            content = getattr(response, "message").content
        except Exception:
            try:
                content = response["message"]["content"]
            except Exception:
                content = str(response)

        # Parse structured response
        parsed = parse_structured_response(content)
        
        return {"raw": response, "text": content, "parsed": parsed}
    except Exception as e:
        raise RuntimeError(
            f"Failed to call Ollama. Make sure:\n"
            f"1. Ollama is running: `ollama serve`\n"
            f"2. Model '{model}' is available: `ollama pull {model}`\n"
            f"3. Model is properly loaded and has vision capabilities\n"
            f"Error: {str(e)}"
        )


def display_image_metadata(uploaded_file, img_pil: Image.Image):
    """Display image metadata in sidebar."""
    st.sidebar.subheader("📊 Image Details")
    
    # Basic info
    st.sidebar.write(f"**Filename:** {uploaded_file.name}")
    st.sidebar.write(f"**Size:** {img_pil.width} × {img_pil.height} px")
    st.sidebar.write(f"**Format:** {img_pil.format}")
    st.sidebar.write(f"**Mode:** {img_pil.mode}")
    
    # File size - use session state bytes if available, otherwise try getvalue()
    try:
        if 'img_bytes' in st.session_state:
            file_size = len(st.session_state.img_bytes)
        else:
            file_size = len(uploaded_file.getvalue())
        
        if file_size > 1024 * 1024:
            size_str = f"{file_size / (1024 * 1024):.1f} MB"
        else:
            size_str = f"{file_size / 1024:.1f} KB"
        st.sidebar.write(f"**File Size:** {size_str}")
    except AttributeError:
        st.sidebar.write(f"**File Size:** Unable to determine")


def main():
    # Header with styling
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; font-size: 2.5rem;">🔍 AI Image Analyzer</h1>
        <p style="color: #f0f0f0; margin: 0.5rem 0 0 0; font-size: 1.2rem;">Powered by Gemma3:4b Multimodal Vision AI</p>
    </div>
    """, unsafe_allow_html=True)

        # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Model info
        st.markdown(f"""
        <div style="background: #f0f8ff; padding: 1rem; border-radius: 5px; border-left: 4px solid #4285f4;">
            <strong>🤖 Vision Model:</strong><br>
            <code>{MODEL}</code><br>
            <small>✨ Multimodal AI with vision capabilities</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")        # Instructions
        st.subheader("📝 Instructions")
        st.markdown("""
        1. **Upload** a JPG/JPEG image
        2. **Customize** the analysis prompt (optional)
        3. **Click** Analyze to get AI insights
        4. **Review** structured results
        """)

    # Main content area
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📤 Upload Image")
        uploaded = st.file_uploader(
            "Choose a JPG or JPEG image file",
            type=["jpg", "jpeg"],
            accept_multiple_files=False,
            help="Supported formats: JPG, JPEG. Max size recommended: 10MB"
        )

        if uploaded is None:
            st.info("👆 Upload an image to get started!")
            
            # Show example/demo section
            st.markdown("---")
            st.subheader("✨ What this app does")
            st.markdown("""
            - 🔍 **Analyzes images** using advanced AI models
            - 📝 **Extracts insights** like objects, scenes, and context
            - 🏷️ **Generates tags** and descriptions automatically
            - 📊 **Provides confidence scores** for reliability
            - 🎨 **Beautiful interface** with structured results
            """)
            return

        # Display uploaded image
        try:
            # Read file bytes once and store in session state to avoid re-reading
            if 'img_bytes' not in st.session_state or st.session_state.get('uploaded_file_name') != uploaded.name:
                st.session_state.img_bytes = uploaded.read()
                st.session_state.uploaded_file_name = uploaded.name
            
            img_bytes = st.session_state.img_bytes
            img_pil = Image.open(io.BytesIO(img_bytes))
            
            st.image(img_pil, caption=f"📷 {uploaded.name}", use_container_width=True)
            
            # Display metadata in sidebar
            display_image_metadata(uploaded, img_pil)
            
        except Exception as e:
            st.error(f"❌ Could not read uploaded file: {e}")
            return

    with col2:
        st.subheader("🎯 Analysis Settings")
        
        # Show selected model
        st.markdown(f"**Using Model:** `{MODEL}`")
        st.caption("🔍 Multimodal vision-capable AI model")
        
        st.markdown("---")
        
        # Customizable prompt
        prompt = st.text_area(
            "What type of analysis do you want to perform?",
            value="What type of analysis do you want to perform?",
            height=150,
            help="Describe what kind of analysis you want the AI to perform on your image"
        )
        
        # Analysis button
        analyze_btn = st.button(
            "🚀 Analyze Image",
            type="primary",
            use_container_width=True
        )

    # Analysis results
    if analyze_btn:
        # Check if we have image bytes stored
        if 'img_bytes' not in st.session_state:
            st.error("❌ No image data found. Please upload an image first.")
            return
            
        with st.spinner(f"🤖 Analyzing with {MODEL}..."):
            try:
                result = call_ollama_analysis(st.session_state.img_bytes, MODEL, prompt)
                parsed = result.get("parsed", {})
                
                st.success("✅ Analysis completed!")
                
                # Create tabs for different views
                tab1, tab2, tab3 = st.tabs(["📋 Summary", "🔍 Detailed Analysis", "⚙️ Raw Data"])
                
                with tab1:
                    # Summary cards
                    if parsed.get("description"):
                        st.markdown(f"""
                        <div style="background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #28a745; margin: 1rem 0;">
                            <h4 style="color: #155724; margin-top: 0;">📝 Description</h4>
                            <p style="color: #155724; margin-bottom: 0; font-size: 1.1rem;">{parsed['description']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Confidence score
                    if parsed.get("confidence"):
                        confidence = parsed["confidence"]
                        color = "#28a745" if confidence >= 80 else "#ffc107" if confidence >= 60 else "#dc3545"
                        st.markdown(f"""
                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 5px; text-align: center; margin: 1rem 0;">
                            <h4 style="color: #333; margin-top: 0;">🎯 Confidence Score</h4>
                            <div style="font-size: 2rem; color: {color}; font-weight: bold;">{confidence}%</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Key observations
                    if parsed.get("key_observations"):
                        st.markdown("### 🔍 Key Observations")
                        for i, obs in enumerate(parsed["key_observations"][:5], 1):
                            if obs.strip():
                                st.markdown(f"**{i}.** {obs}")
                
                with tab2:
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        # Objects detected
                        if parsed.get("objects"):
                            st.markdown("### 🎯 Objects Detected")
                            objects = parsed["objects"] if isinstance(parsed["objects"], list) else [parsed["objects"]]
                            for obj in objects[:10]:
                                if obj.strip():
                                    st.markdown(f"• {obj}")
                        
                        # Full observations list
                        if parsed.get("key_observations"):
                            st.markdown("### 🔍 All Observations")
                            for obs in parsed["key_observations"]:
                                if obs.strip():
                                    st.markdown(f"• {obs}")
                    
                    with col_b:
                        # Tags
                        if parsed.get("tags"):
                            st.markdown("### 🏷️ Suggested Tags")
                            tags = parsed["tags"] if isinstance(parsed["tags"], list) else [parsed["tags"]]
                            tag_html = ""
                            for tag in tags[:15]:
                                if tag.strip():
                                    tag_html += f'<span style="background: #e3f2fd; color: #1976d2; padding: 0.2rem 0.5rem; margin: 0.2rem; border-radius: 15px; font-size: 0.9rem; display: inline-block;">{tag.strip()}</span>'
                            st.markdown(tag_html, unsafe_allow_html=True)
                        
                        # Timestamp
                        st.markdown("### ⏰ Analysis Info")
                        st.write(f"**Completed:** {datetime.now().strftime('%H:%M:%S')}")
                        st.write(f"**Model:** {MODEL}")
                
                with tab3:
                    st.subheader("📄 Full Response Text")
                    st.text_area("Model Output", result.get("text", ""), height=300)
                    
                    st.subheader("🔧 Raw Response Object")
                    with st.expander("Show raw response data"):
                        try:
                            if hasattr(result.get("raw"), '__dict__'):
                                st.json(result["raw"].__dict__)
                            else:
                                st.text(str(result.get("raw")))
                        except Exception:
                            st.text(str(result.get("raw")))

            except ImportError:
                st.error("❌ Ollama package not installed")
                st.info("💡 Install with: `pip install ollama`")
            except ConnectionError:
                st.error("❌ Cannot connect to Ollama service")
                st.info("💡 Make sure Ollama is running with: `ollama serve`")
            except RuntimeError as e:
                st.error(f"❌ Analysis failed: {str(e)}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
                st.info("💡 Try restarting the app or check the console for details")


if __name__ == "__main__":
    main()
