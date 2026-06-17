from groq import Groq
from dotenv import load_dotenv

import os
import random

load_dotenv()
print("USING GROQ QUESTION GENERATOR")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_questions(topic):

    try:

        seed = random.randint(
            1,
            100000
        )

        prompt = f"""
Topic: {topic}

Generate EXACTLY 5 advanced assessment questions.

STRICT RULES:

DO NOT generate:

- What is {topic}?
- Define {topic}
- Why is {topic} important?
- List applications of {topic}

Instead generate:

1. Scenario-based questions
2. Analytical questions
3. Problem-solving questions
4. Real-world application questions
5. Comparison questions

Assume the audience already knows the basics.

Return ONLY:

Question: ...
Answer: ...

Question: ...
Answer: ...

Question: ...
Answer: ...

Question: ...
Answer: ...

Question: ...
Answer: ...
"""
        print("GENERATING:", topic)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=1
        )

        text = (
            response
            .choices[0]
            .message
            .content
        )

        print("\n===== GROQ RESPONSE =====\n")
        print(text)
        print("\n=========================\n")

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
                            "question": current_question,
                            "answer": answer
                        }
                    )

                    current_question = None

        if len(questions) >= 5:

            return questions[:5]

        raise Exception(
            "Could not parse model response."
        )

    except Exception as e:

        print(
            "QUESTION GENERATION ERROR:",
            e
        )

        return [

            {
                "question":
                f"Explain a practical application of {topic}.",

                "answer":
                f"A real-world application of {topic}."
            },

            {
                "question":
                f"What challenges are associated with {topic}?",

                "answer":
                f"Common limitations and challenges."
            },

            {
                "question":
                f"How is {topic} used in industry?",

                "answer":
                f"Industrial use cases of {topic}."
            },

            {
                "question":
                f"Compare {topic} with a related concept.",

                "answer":
                f"Major similarities and differences."
            },

            {
                "question":
                f"What factors influence the effectiveness of {topic}?",

                "answer":
                f"Key influencing factors."
            }

        ]