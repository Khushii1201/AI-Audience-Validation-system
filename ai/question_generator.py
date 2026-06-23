import ollama
import random


def generate_questions(topic):

    try:

        seed = random.randint(
            1,
            100000
        )

        prompt = f"""
        Random Seed: {seed}

        Topic: {topic}

        Generate EXACTLY 5 advanced assessment questions.

        Do NOT ask:
        - What is {topic}
        - Why is {topic} important

        Include:
        - Scenario based questions
        - Analytical questions
        - Application questions

        Return ONLY:

        Question: ...

        Answer: ...
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

        print(text)

        questions = []

        current_question = None

        for line in text.splitlines():

            line = line.strip()

            if line.startswith("Question:"):

                current_question = (
                    line.replace(
                        "Question:",
                        ""
                    ).strip()
                )

            elif line.startswith("Answer:"):

                answer = (
                    line.replace(
                        "Answer:",
                        ""
                    ).strip()
                )

                if current_question:

                    questions.append(
                        {
                            "question":current_question,
                            "answer":answer
                        }
                    )

                    current_question = None

        return questions[:5]

    except Exception as e:

        print(e)

        return []