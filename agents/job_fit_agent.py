from tools.gemini_client import get_gemini_client
from tools.prompts import JOB_FIT_PROMPT
from utils.helpers import extract_markdown_content

def score_job_fit(resume_text: str, target_role: str, job_description: str) -> str:
    """
    Scores the resume against a specific job description or target role.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = JOB_FIT_PROMPT | llm
    
    # If no job description is provided, use the target role
    job_context = job_description if job_description.strip() else f"General requirements for a {target_role} role."
    
    response = chain.invoke({
        "resume_text": resume_text,
        "job_description": job_context
    })
    return extract_markdown_content(response.content)
