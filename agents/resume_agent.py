from tools.gemini_client import get_gemini_client
from tools.prompts import RESUME_ANALYZER_PROMPT
from utils.helpers import extract_markdown_content

def analyze_resume(resume_text: str) -> str:
    """
    Analyzes the resume for strengths, weaknesses, and ATS friendliness.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = RESUME_ANALYZER_PROMPT | llm
    
    response = chain.invoke({"resume_text": resume_text})
    return extract_markdown_content(response.content)
