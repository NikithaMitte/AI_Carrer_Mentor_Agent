from tools.gemini_client import get_gemini_client
from tools.prompts import INTERVIEW_PROMPT
from utils.helpers import extract_markdown_content

def generate_interview_questions(resume_text: str, target_role: str) -> str:
    """
    Generates interview questions and model answers based on target role and resume.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = INTERVIEW_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "target_role": target_role
    })
    return extract_markdown_content(response.content)
