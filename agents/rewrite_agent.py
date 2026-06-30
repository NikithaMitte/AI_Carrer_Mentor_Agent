from tools.gemini_client import get_gemini_client
from tools.prompts import REWRITE_PROMPT
from utils.helpers import extract_markdown_content

def rewrite_resume(resume_text: str) -> str:
    """
    Rewrites the resume for better ATS compatibility.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = REWRITE_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text
    })
    return extract_markdown_content(response.content)
