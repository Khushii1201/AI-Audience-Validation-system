import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.db import get_connection

st.set_page_config(
    page_title="Learning Insights",
    layout="wide"
)

st.title(" Learning Insights")

st.markdown("""
Identify concepts that require reinforcement based on audience performance.
""")

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

if len(results) == 0:

    st.info(
        "No responses available."
    )

else:

    weak_count = 0
    moderate_count = 0
    strong_count = 0

    for question, avg_score in results:

        if avg_score < 8:

            weak_count += 1

        elif avg_score < 15:

            moderate_count += 1

        else:

            strong_count += 1

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            " Weak Concepts",
            weak_count
        )

    with col2:

        st.metric(
            " Moderate Concepts",
            moderate_count
        )

    with col3:

        st.metric(
            " Strong Concepts",
            strong_count
        )

    st.divider()

    for question, avg_score in results:

        with st.container(border=True):

            st.write(
                f"Question: {question}"
            )

            st.metric(
                "Average Score",
                f"{avg_score:.1f}/20"
            )

            if avg_score < 8:

                st.error(
                    " Needs Reinforcement"
                )

                st.write(
                    "Most participants struggled with this concept."
                )

            elif avg_score < 15:

                st.warning(
                    " Moderate Understanding"
                )

                st.write(
                    "Some participants understood the concept, but improvement is possible."
                )

            else:

                st.success(
                    " Strong Understanding"
                )

                st.write(
                    "Most participants demonstrated good understanding."
                )