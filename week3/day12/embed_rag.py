import os
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2') #384
text = "I love programming in Python."

embedding = model.encode(text)
print(f"Embedding shape: {embedding.shape}")
print(embedding)