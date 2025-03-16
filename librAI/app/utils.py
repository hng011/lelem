from enum import Enum
from .config import OPENAI_API_KEY, OPEN_ROUTER_API_KEY

def check_api_keys():
    if not (OPENAI_API_KEY):
        raise ValueError("Invalid API Key!!!")

    if not (OPEN_ROUTER_API_KEY):
        raise ValueError("Invalid API Key!!!")    
    
class PromptType(Enum):
    SYSTEM_PROMPT_1 = "You are a helpful assistant for a library called LibrAI Give a short, corteous answers, no more than 1 sentence and always be accurate. If you do not know the answers, just say so"