from app.utils import check_api_keys, PromptType
from app.models import LLM
import gradio as gr


if __name__=="__main__":
    check_api_keys()
    chat = LLM(system_prompt=PromptType.SYSTEM_PROMPT_1.value, model="gpt-4o-mini")
    gr.ChatInterface(fn=chat.chat_openai).launch()