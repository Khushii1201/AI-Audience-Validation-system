import streamlit as st

from database.db import (
    create_tables,
    get_connection
)

create_tables()

st.title(
    "Audience Understanding Dashboard"
)

conn = get_connection()

cursor = conn.cursor()

# Participant Scores
cursor.execute("""
SELECT
    user_name,
    SUM(score)
FROM responses
GROUP BY user_name
""")

results = cursor.fetchall()

st.subheader(
    "Participant Scores"
)
cursor.execute("""
SELECT COUNT(*)
FROM responses
""")

response_count = cursor.fetchone()[0]

st.metric(
    "Total Responses",
    response_count
)

total_scores = []

for user, score in results:

    total_scores.append(score)

    st.write(
        f"{user} : {score}"
    )

# Average Score

if len(total_scores) > 0:

    average_score = (
        sum(total_scores)
        /
        len(total_scores)
    )

else:

    average_score = 0

st.metric(
    "Average Score",
    f"{average_score:.2f}"
)

# Clarity Score

st.metric(
    "Clarity Score",
    f"{average_score:.2f}%"
)

conn.close()