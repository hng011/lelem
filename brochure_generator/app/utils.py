import os
from .config import OPENAI_API_KEY, OPEN_ROUTER_API_KEY
from .models import Website, LLM

def check_api_keys():
    if not (OPENAI_API_KEY):
        raise ValueError("Invalid API Key!!!")

    if not (OPEN_ROUTER_API_KEY):
        raise ValueError("Invalid API Key!!!")
    
    
def summarize(content: Website, model: str, platform: int):
    system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
                    and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
                    Include details of company culture, customers and careers/jobs if you have the information."

    user_prompt = f"You are looking at a company called {content.title} \
                    Here are the content of its landing page and use this information as a source to build \
                    a short and interesting brochure of the company in markdown\n \
                    {content.text[:5_000]}"
    
    if platform == 1:
        return LLM(system_prompt=system_prompt, user_prompt=user_prompt, model=model).call_openai()
    elif platform == 2:
        return LLM(system_prompt=system_prompt, user_prompt=user_prompt, model=model).call_openrouter()
    else:
        return "Please decide the platfrom you want to use"
    

def to_markdown(content: str, filename:str = "brochure.md", path: str = "./output"):
    if not os.path.exists(path):
        os.makedirs(path)
    
    with open(os.path.join(path, filename), "w") as f:
        f.write(content)