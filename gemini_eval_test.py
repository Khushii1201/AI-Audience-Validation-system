from ai.groq_evaluator import evaluate_answer

score, feedback = evaluate_answer(
    question=
    "What is a Primary Key?",

    correct_answer=
    "A unique identifier for a record.",

    user_answer=
    "A primary key uniquely identifies every row in a table."
)

print("Score:", score)
print("Feedback:", feedback)