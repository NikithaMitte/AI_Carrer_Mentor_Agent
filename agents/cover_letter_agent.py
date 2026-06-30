from tools.gemini_client import get_gemini_client
from tools.prompts import COVER_LETTER_PROMPT
from utils.helpers import extract_markdown_content

def generate_cover_letter(resume_text: str, job_description: str) -> str:
    """
    Generates a personalized cover letter based on resume and job description.
    """
    if not resume_text:
        return "Please upload a resume first."
    if not job_description:
        return "Please provide a job description to generate the cover letter."
        
    llm = get_gemini_client()
    chain = COVER_LETTER_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "job_description": job_description
    })
    return extract_markdown_content(response.content)
