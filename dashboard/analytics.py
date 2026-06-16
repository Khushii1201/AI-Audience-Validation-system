import streamlit as st

from database.db import (
    create_tables,
    get_connection
)

create_tables()

st.title("Analytics Dashboard")

conn = get_connection()
cursor = conn.cursor()

# Total Participants
cursor.execute("""
SELECT COUNT(DISTINCT user_name)
FROM responses
""")

participants = cursor.fetchone()[0]

# Average Score
cursor.execute("""
SELECT AVG(score)
FROM responses
""")
cursor.execute("""
SELECT
    q.question,
    AVG(r.score)
    FROM responses r
    JOIN questions q
    ON r.question_id = q.question_id
    GROUP BY q.question
""")

question_scores = cursor.fetchall()

st.subheader("Question Accuracy")

for question, score in question_scores:

    st.write(
        f"{question} : {score:.2f}%"
    )

avg_score = cursor.fetchone()[0]

if avg_score is None:
    avg_score = 0

st.metric(
    "Total Participants",
    participants
)

st.metric(
    "Average Score",
    f"{avg_score:.2f}"
)

conn.close()