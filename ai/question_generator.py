from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_questions(topic):

    prompt = f"""
Generate exactly 5 questions on {topic}.

Include:
- 2 MCQs
- 2 True/False
- 1 Descriptive Question

Provide answers.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text