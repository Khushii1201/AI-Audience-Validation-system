import ollama
import re


def evaluate_answer(
        question,
        expected_answer,
        student_answer
):

    try:

        prompt = f"""
        Question:
        {question}

        Expected Answer:
        {expected_answer}

        Student Answer:
        {student_answer}

        Score answer from 0-20.

        Return EXACTLY:

        Score: X

        Feedback: Y
        """

        response = ollama.chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        text = (
            response["message"]["content"]
        )

        score_match = re.search(
            r"Score:\s*(\d+)",
            text
        )

        score = 10

        if score_match:

            score = int(
                score_match.group(1)
            )

        feedback_match = re.search(
            r"Feedback:\s*(.*)",
            text,
            re.DOTALL
        )

        feedback = (
            feedback_match.group(1)
            if feedback_match
            else "Evaluation completed."
        )

        return (
            score,
            feedback
        )

    except Exception as e:

        print(e)

        return (
            0,
            "Evaluation failed."
        )