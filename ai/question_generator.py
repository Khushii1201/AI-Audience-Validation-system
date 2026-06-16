from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_questions(topic):

    try:

        prompt = f"""
        Generate exactly 5 interview-style questions and answers on the topic: {topic}

        Return ONLY in this format:

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>

        Question: <question>
        Answer: <answer>
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text

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

        if len(questions) > 0:

            return questions

        raise Exception(
            "No questions generated"
        )

    except Exception as e:

        print(
            "Gemini Error:",
            e
        )

        return [
            {
                "question":
                f"What is {topic}?",

                "answer":
                f"Definition of {topic}"
            },

            {
                "question":
                f"Why is {topic} important?",

                "answer":
                f"Importance of {topic}"
            },

            {
                "question":
                f"What are the applications of {topic}?",

                "answer":
                f"Applications of {topic}"
            },

            {
                "question":
                f"What are the advantages of {topic}?",

                "answer":
                f"Advantages of {topic}"
            },

            {
                "question":
                f"What are the challenges in {topic}?",

                "answer":
                f"Challenges in {topic}"
            }
        ]