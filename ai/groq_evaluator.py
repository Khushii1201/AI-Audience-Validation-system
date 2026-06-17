from groq import Groq
from dotenv import load_dotenv

import os
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_answer(
        question,
        correct_answer,
        student_answer
):

    try:

        prompt = f"""
        You are an examiner.

        Question:
        {question}

        Expected Answer:
        {correct_answer}

        Student Answer:
        {student_answer}

        Evaluate the student answer.

        Give:

        Score: X

        where X is between 0 and 20.

        Feedback: brief explanation.

        Example:

        Score: 16

        Feedback: Good understanding but missed some key points.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        result = (
            response
            .choices[0]
            .message
            .content
        )

        print("\n===== EVALUATION =====\n")
        print(result)
        print("\n======================\n")

        score_match = re.search(
            r"Score:\s*(\d+)",
            result
        )

        if score_match:

            score = int(
                score_match.group(1)
            )

            score = max(
                0,
                min(
                    score,
                    20
                )
            )

        else:

            score = 10

        feedback_match = re.search(
            r"Feedback:\s*(.*)",
            result,
            re.DOTALL
        )

        if feedback_match:

            feedback = (
                feedback_match
                .group(1)
                .strip()
            )

        else:

            feedback = (
                "Evaluation completed."
            )

        return (
            score,
            feedback
        )

    except Exception as e:

        print(
            "EVALUATION ERROR:",
            e
        )

        return (
            0,
            "Unable to evaluate answer."
        )