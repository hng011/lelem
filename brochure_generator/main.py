import time
from app.models import Website
from app.utils import to_markdown, summarize, check_api_keys
    
    
if __name__=="__main__":
    web = Website("https://github.com/hng011")

    try:
        
        check_api_keys()
        
        start_time = time.time()
        to_markdown(
            content=summarize(content=web, model="qwen/qwq-32b:free", platform=2),
        )
        end_time = time.time()
        
        print(f"Brochure created successfully | {end_time - start_time} seconds")
    
    except Exception as e:
        print(e)