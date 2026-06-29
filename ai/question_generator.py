import ollama
import time


# ----------------------------------------------------
# Generate AI Questions
# ----------------------------------------------------

def generate_questions(
    topic,
    difficulty="Medium"
):

    start = time.time()

    try:

        prompt = f"""
You are an expert university professor.

Topic:
{topic}

Difficulty:
{difficulty}

Generate EXACTLY 5 interview-style assessment questions.

Rules:

1. Difficulty must match "{difficulty}"

2. Never ask:
- What is {topic}?
- Define {topic}.
- Why is {topic} important?

3. Prefer:
- Scenario-based
- Application-based
- Analytical
- Critical thinking
- Real-world problem solving

4. Keep every question under 30 words.

5. Keep every answer under 60 words.

Return ONLY in this format.

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

        print("=" * 60)
        print(f"Generating {difficulty} questions for {topic}")
        print("=" * 60)

        response = ollama.chat(

            model="qwen2.5:3b",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        text = response["message"]["content"]

        print(text)

        questions = []

        current_question = None

        for line in text.splitlines():

            line = line.strip()

            if not line:

                continue

            if line.startswith("Question:"):

                current_question = line.replace(
                    "Question:",
                    ""
                ).strip()

            elif line.startswith("Answer:"):

                answer = line.replace(
                    "Answer:",
                    ""
                ).strip()

                if current_question:

                    questions.append(

                        {

                            "question": current_question,

                            "answer": answer

                        }

                    )

                    current_question = None

        if len(questions) != 5:

            raise Exception(
                f"Expected 5 questions, got {len(questions)}"
            )

        print(
            f"Finished in {time.time()-start:.2f}s"
        )

        return questions

    except Exception as e:

        print("Question Generation Error")
        print(e)

        return [

            {

                "question":
                f"Explain one practical application of {topic}.",

                "answer":
                f"A practical real-world use of {topic}."

            },

            {

                "question":
                f"Compare {topic} with another related concept.",

                "answer":
                f"Discuss similarities and differences."

            },

            {

                "question":
                f"What challenges are faced while implementing {topic}?",

                "answer":
                f"Major limitations and implementation issues."

            },

            {

                "question":
                f"Describe an industrial use case of {topic}.",

                "answer":
                f"Explain where it is used in industry."

            },

            {

                "question":
                f"How would you solve a real-world problem using {topic}?",

                "answer":
                f"Describe the approach and expected outcome."

            }

        ]