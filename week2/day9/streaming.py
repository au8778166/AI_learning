import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

prompt = """
Explain the concept of Agentic AI in detail
"""
message = {
    "role": "user",
    "content": prompt   
}

stream = client.chat.completions.create(model=model, messages=[message], stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)

