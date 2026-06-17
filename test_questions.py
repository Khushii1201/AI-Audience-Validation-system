from ai.question_generator import generate_questions

questions = generate_questions(
    "Artificial Intelligence"
)

for q in questions:
    print(q)