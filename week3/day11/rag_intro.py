import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)
model  = "openai/gpt-oss-120b"
#step1 knowledge base
knowledge_base = {
    "age" : "The age of Abhishek is 21 years old.",
    "net worth" : "The net worth of Abhishek is 1 million dollars.",
}

#step2 retrieval function
def retrieve_info(question):
    question = question.lower()
    if "age" in question:
        return knowledge_base["age"]    
    elif "net worth" in question:
        return knowledge_base["net worth"]
    else:
        return None
def ask_llm(question):
    context = retrieve_info(question)

    sys_prompt = f"""
     answer in one line. Answer only based on this context. Do not hallucinate. Context: {context}
     """

    system_message = {
        "role": "system",
        "content": sys_prompt
    }
    message = {
        "role": "user",
        "content": question
    }
    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

question = "What is the age of Abhishek?"
print(ask_llm(question))
 