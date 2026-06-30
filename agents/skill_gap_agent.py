from tools.gemini_client import get_gemini_client
from tools.prompts import SKILL_GAP_PROMPT
from utils.helpers import extract_markdown_content

def analyze_skill_gap(resume_text: str, target_role: str) -> str:
    """
    Compares resume skills with target role requirements.
    """
    if not resume_text:
        return "Please upload a resume first."
        
    llm = get_gemini_client()
    chain = SKILL_GAP_PROMPT | llm
    
    response = chain.invoke({
        "resume_text": resume_text,
        "target_role": target_role
    })
    return extract_markdown_content(response.content)
