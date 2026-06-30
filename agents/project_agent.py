from tools.gemini_client import get_gemini_client
from tools.prompts import PROJECT_PROMPT
from utils.helpers import extract_markdown_content

def recommend_projects(resume_text: str, target_role: str) -> str:
    """
    Recommends projects to build the portfolio for a target role.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = PROJECT_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "target_role": target_role
    })
    return extract_markdown_content(response.content)
