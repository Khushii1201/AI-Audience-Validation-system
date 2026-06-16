import streamlit as st

from database.db import get_connection

st.title(
    "Question Analytics"
)

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT
    q.question,
    AVG(r.score)
FROM responses r
JOIN questions q
ON r.question_id = q.question_id
GROUP BY q.question
""")

results = cursor.fetchall()

conn.close()

for question, avg_score in results:

    st.write(
        f"{question}"
    )

    st.progress(
        int(avg_score)
    )

    st.write(
        f"Average Score: {avg_score}"
    )