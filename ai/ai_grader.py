from openai import OpenAI
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def grade_answer(
        question,
        correct_answer,
        user_answer
):

    prompt = f"""
You are an expert evaluator.

Question:
{question}

Correct Answer:
{correct_answer}

User Answer:
{user_answer}

Return JSON:

{{
"score": 0-100,
"feedback": "short explanation"
}}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    text = response.output_text

    try:

        result = json.loads(text)

        return result

    except:

        return {
            "score": 0,
            "feedback":
            "Unable to evaluate"
        }