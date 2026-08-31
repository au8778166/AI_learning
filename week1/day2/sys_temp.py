import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API error")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role="user"
prompt="Suggest me a single brand name for my new food company"
#system message to set the context for the conversation
message_system = {
    "role" : "system",
    "content" : "You are a brand manager who suggests me a brand name for my new food company"
}
#temperature message to set the context for the conversation

message = {
    "role" : role,
    "content" : prompt
}
messages = [message_system, message]
response = client.chat.completions.create(model=model,messages=messages,temperature=2)
response_text = response.choices[0].message.content
print(response_text)