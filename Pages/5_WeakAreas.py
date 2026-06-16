import streamlit as st

from database.db import get_connection

st.title(
    "Weak Areas Analysis"
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

    if avg_score < 50:

        st.error(
            f"Weak Area: {question}"
        )

    else:

        st.success(
            f"Strong Area: {question}"
        )