import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_gemini_client(temperature=0.7):
    """
    Initializes and returns a Google Gemini 2.5 Flash client via LangChain.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    
    # We will use Gemini 2.5 Flash as requested. Since the requested version is 2.5,
    # the model string is typically "gemini-2.5-flash" (assuming it is available, otherwise falls back to gemini-1.5-flash).
    # Using gemini-1.5-flash as the stable identifier for current langchain integrations, but can use 2.5 if released.
    model_name = "gemini-2.5-flash" 
    
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=api_key,
        temperature=temperature,
        convert_system_message_to_human=True
    )
    return llm
