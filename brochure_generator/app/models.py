from openai import OpenAI
from bs4 import BeautifulSoup

import requests
import os
import json

from .config import headers, OPENAI_API_KEY, OPEN_ROUTER_API_KEY


class Website:    
    def __init__(self, url):
        self.url = url
        self.body = requests.get(url, headers=headers).content
        
        soup = BeautifulSoup(markup=self.body, features="lxml")
        self.title = soup.title.text if soup.title.text else "No Title Found"
        if soup.body: 
            for irrelevant in soup.body(["script", "style", "img", "input", "svg"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator='\n', strip=True)
        else:
            self.text = ""
        self.links = [link for link in [link.get("href") for link in soup.find_all('a')] if link] # remove null values

    def get_content(self):
        return f"Webpage Title: {self.title}\nWebpage Content:\n{self.text}"


class LLM:
    def __init__(self, system_prompt, user_prompt, model):
        self.system_prompt = system_prompt
        self.user_prompt = user_prompt
        self.model = model
        
    def call_openai(self):
        openai = OpenAI(api_key=OPENAI_API_KEY)

        response = openai.chat.completions.create(
            model = self.model,
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt},
            ] 
        )
        
        return response.choices[0].message.content

    def call_openrouter(self):
        try:
            response = requests.post(
                url=os.getenv("OPENROUTER_ENDPOINT"),
                headers={
                    "Authorization": f"Bearer {OPEN_ROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": self.user_prompt},
                    ],
                })
            )
            
            return str(response.json()["choices"][0]["message"]["content"]).strip()
        
        except Exception as e:
            return e       