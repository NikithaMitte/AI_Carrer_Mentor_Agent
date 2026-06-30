import streamlit as st
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide Streamlit developer elements but KEEP the main menu (Settings, Print, etc.)
hide_st_style = """
            <style>
            /* Hide the default Streamlit footer (Made with Streamlit) */
            footer {visibility: hidden;}
            
            /* Hide the 'Manage app' button on Streamlit Community Cloud */
            [data-testid="manage-app-button"] {display: none !important;}
            #manage-app-button {display: none !important;}
            
            /* Hide the Deploy button */
            .stDeployButton {display: none !important;}
            
            /* Hide the Streamlit Cloud GitHub/Fork/Share icons in the toolbar */
            [data-testid="stToolbarActions"] {display: none !important;}
            [data-testid="stToolbarActionButton"] {display: none !important;}
            .stActionButton {display: none !important;}
            
            /* Hide the 'Hosted with Streamlit' badge */
            .viewerBadge_container {display: none !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

from utils.constants import AVAILABLE_FEATURES
from utils.helpers import render_sidebar
from tools.pdf_reader import extract_text_from_pdf
from tools.resume_parser import parse_resume
from agents.supervisor import build_graph

# Caching the PDF parsing so it's lightning fast on subsequent runs
@st.cache_data
def process_pdf_cached(file_bytes):
    import io
    # We pass the bytes to PyPDF2 inside the reader to cache effectively
    pdf_file = io.BytesIO(file_bytes)
    raw_text = extract_text_from_pdf(pdf_file)
    if not raw_text:
        return None
    return parse_resume(raw_text)

def main():
    st.title("🧠 AI Career Mentor Agent")
    st.markdown("Your personal AI-powered career counselor, resume reviewer, and interview prep assistant.")
    
    # Render Sidebar
    uploaded_file, target_role = render_sidebar()
    
    # Main content area
    st.markdown("### Choose an AI Feature")
    
    # Selectbox for features
    selected_feature = st.selectbox("What would you like to do today?", list(AVAILABLE_FEATURES.keys()))
    st.info(AVAILABLE_FEATURES[selected_feature])
    
    # Show Job Description input if required by the feature
    job_description = ""
    if selected_feature in ["Cover Letter Generator", "Job Fit Scorer"]:
        st.markdown("#### Job Description (Optional for Job Fit)")
        job_description = st.text_area("Paste the Job Description here (or leave blank to use target role):", height=200)
    
    if st.button("🚀 Run AI Agent"):
        if not uploaded_file:
            st.error("Please upload your Resume (PDF) in the sidebar first.")
            return
            
        if selected_feature == "Cover Letter Generator" and not job_description.strip():
            st.error("Please provide a Job Description to generate a Cover Letter.")
            return
            
        if not os.getenv("GEMINI_API_KEY"):
            st.error("GEMINI_API_KEY is missing. Please check your .env file.")
            return
            
        with st.spinner(f"Agents are orchestrating '{selected_feature}'..."):
            try:
                # 1. Extract and parse resume (Cached for speed)
                file_bytes = uploaded_file.getvalue()
                resume_text = process_pdf_cached(file_bytes)
                
                if not resume_text:
                    st.error("Failed to read PDF. Please ensure it's a valid text-based PDF.")
                    return
                
                # 2. Build and run LangGraph workflow
                graph = build_graph()
                
                # Initial state
                state = {
                    "resume_text": resume_text,
                    "target_role": target_role,
                    "job_description": job_description,
                    "selected_feature": selected_feature,
                    "final_response": ""
                }
                
                # Invoke graph
                result = graph.invoke(state)
                
                # 3. Display Result
                st.success("✅ Analysis Complete!")
                st.markdown("---")
                # Using st.write to display nicely
                st.write(result["final_response"])
                
                # Bonus: Provide download button
                st.download_button(
                    label="📥 Download AI Report",
                    data=result["final_response"],
                    file_name=f"{selected_feature.lower().replace(' ', '_')}_report.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"An error occurred during agent execution: {str(e)}")

if __name__ == "__main__":
    main()
