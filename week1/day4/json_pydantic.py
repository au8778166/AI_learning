import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API error")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"
role="user"

from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()
response_format = {
    "type" : "json_object",
}
system_prompt = f"""
You are a helpful assistant that extracts personal information from customer tickets in json format based on the following schema: {schema}
"""
message_system = {
    "role" : "system",
    "content" : system_prompt
}
text = "Hello ji My name is Abhishek Upadhyay, I have purchased Headphone of boat it's sound quality is not so perfect. My address is Jhokhipur, my phone number is 546897123, au8778166@gmail.com"
prompt=f"""
This is a customer ticket. Please Extract the personal informatiom from this {text}
"""
message = {
    "role" : role,
    "content" : prompt
}
messages = [message_system,message]
response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)
response_text = response.choices[0].message.content
print(response_text)

import json
raw_json=response_text
data_file = json.loads(raw_json)    
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)




