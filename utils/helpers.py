import re
import streamlit as st

def clean_text(text: str) -> str:
    """Cleans raw text by removing extra spaces and special characters."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,;:()\-]', '', text)
    return text.strip()

def render_sidebar():
    """Renders the common sidebar elements in Streamlit."""
    st.sidebar.title("🧠 AI Career Mentor")
    st.sidebar.markdown("---")
    
    uploaded_file = st.sidebar.file_uploader("1. Upload Resume (PDF)", type=["pdf"])
    
    from utils.constants import ROLES
    target_role = st.sidebar.selectbox("2. Select Target Role", ROLES)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Powered by Google Gemini 2.5 Flash & LangGraph")
    
    return uploaded_file, target_role

def extract_markdown_content(text: str) -> str:
    """Extracts content inside markdown code blocks if present, otherwise returns raw text."""
    match = re.search(r'```markdown\n(.*?)\n```', text, re.DOTALL)
    if match:
        return match.group(1)
    
    match_json = re.search(r'```json\n(.*?)\n```', text, re.DOTALL)
    if match_json:
        return match_json.group(1)
        
    return text
