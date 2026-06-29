import json
import ollama


# ----------------------------------------------------
# Evaluate Student Answer
# ----------------------------------------------------

def evaluate_answer(
    question,
    expected_answer,
    student_answer
):

    try:

        prompt = f"""
You are an expert university examiner.

Evaluate the student's answer.

Question:
{question}

Expected Answer:
{expected_answer}

Student Answer:
{student_answer}

Evaluation Criteria:

1. Conceptual correctness
2. Technical accuracy
3. Completeness
4. Clarity
5. Relevance

Give a score from 0 to 20.

Return ONLY valid JSON.

Example:

{{
    "score": 18,
    "feedback": "Good understanding of the concept.",
    "strength": "Explained the main idea correctly.",
    "improvement": "Add one real-world example."
}}

Do NOT return markdown.
Do NOT return explanation.
Return ONLY JSON.
"""

        response = ollama.chat(

            model="qwen2.5:3b",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        text = response["message"]["content"].strip()

        print("\n========== RAW AI RESPONSE ==========")
        print(text)
        print("=====================================\n")

        # Remove markdown if model adds it
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        result = json.loads(text)

        score = int(result.get("score", 0))

        score = max(
            0,
            min(score, 20)
        )

        feedback = result.get(
            "feedback",
            "No feedback provided."
        )

        strength = result.get(
            "strength",
            "Not available."
        )

        improvement = result.get(
            "improvement",
            "No suggestions."
        )

        feedback = (
            f"✅ Strength: {strength}\n\n"
            f"💬 Feedback: {feedback}\n\n"
            f"📌 Improvement: {improvement}"
        )

        return (
            score,
            feedback
        )

    except Exception as e:

        print("Evaluation Error:")
        print(e)

        return (
            0,
            "AI evaluation failed. Please try again."
        )