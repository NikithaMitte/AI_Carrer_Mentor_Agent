from tools.gemini_client import get_gemini_client
from tools.prompts import SALARY_PROMPT
from utils.helpers import extract_markdown_content

def negotiate_salary(resume_text: str, target_role: str) -> str:
    """
    Provides salary negotiation scripts and market value.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = SALARY_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "target_role": target_role
    })
    return extract_markdown_content(response.content)
