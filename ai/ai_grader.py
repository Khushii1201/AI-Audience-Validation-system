from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def grade_answer(
        question,
        expected_answer,
        user_answer
):

    prompt = f"""
    Question:
    {question}

    Expected Answer:
    {expected_answer}

    User Answer:
    {user_answer}

    Give score only from 0 to 100.
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    try:
        return int(
            response.output_text.strip()
        )
    except:
        return 0