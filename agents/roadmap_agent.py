from tools.gemini_client import get_gemini_client
from tools.prompts import ROADMAP_PROMPT
from utils.helpers import extract_markdown_content

def generate_roadmap(resume_text: str, target_role: str) -> str:
    """
    Generates an 8-week learning roadmap based on the current skills and target role.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = ROADMAP_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "target_role": target_role
    })
    return extract_markdown_content(response.content)
