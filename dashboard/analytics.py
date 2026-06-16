# test_openai.py

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Generate 2 questions about Python"
)

print(response.output_text)