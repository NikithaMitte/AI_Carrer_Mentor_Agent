from utils.helpers import clean_text

def parse_resume(raw_text: str) -> str:
    """
    Cleans and structures raw resume text for the LLM.
    In a more advanced setup, this could use NLP/Regex to extract specific
    sections (Education, Experience). For our AI Agent, providing cleaned 
    full text allows the LLM to extract context directly.
    """
    if not raw_text:
        return ""
    
    cleaned = clean_text(raw_text)
    return cleaned
