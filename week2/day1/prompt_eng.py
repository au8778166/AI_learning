import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    response = client.chat.completions.create(model=model,messages=[message])
    return response.choices[0].message.content

bad_prompt = """
#ROle
You are a helpful Assistant that classifies user complaints into categories.
#TASK
Classify the following user complaint into one of the  categories:
#Constaraints
- The categories are: "Technical Issues", "Billing Issues", "Refund Issues"
#OUTPUT FORMAT
The output should be a single word that is one of the categories listed above.
#FALLBACK
If the complaint does not fit into any of the categories, output "Other".
This is a user complaint:
My laptop is not working properly and keeps crashing.if there is a way to fix it.
"""

print(llm_ans(bad_prompt))