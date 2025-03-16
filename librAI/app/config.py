import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")