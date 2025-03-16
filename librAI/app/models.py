from .config import OPENAI_API_KEY
from openai import OpenAI
from .llm_tools.openai_tools import openai_tool_functions
from .llm_tools.tool_utils import handle_tool_call

class LLM:
    def __init__(self, system_prompt, model):
        self.system_prompt = system_prompt
        self.model = model
        
    
    def chat_openai(self, user_message, history):
        openai = OpenAI(api_key=OPENAI_API_KEY)
        
        messages = [
            {"role": "system", "content": self.system_prompt}
        ]

        for u, a in history:
            messages.append({"role":"user", "content":u})
            messages.append({"role":"assistant", "content":a})

        messages.append({"role": "user", "content": user_message})
        print(messages)
        
        response = openai.chat.completions.create(
            model = self.model,
            messages = messages,
            tools=openai_tool_functions
        )
        
        if response.choices[0].finish_reason == "tool_calls":
            msg = response.choices[0].message
            response = handle_tool_call(msg)
            messages.append(msg)
            messages.append(response)
            response = openai.chat.completions.create(model = self.model, messages=messages)
        
        return response.choices[0].message.content