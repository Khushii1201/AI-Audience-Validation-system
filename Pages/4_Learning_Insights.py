import streamlit as st

from database.db import get_connection

st.set_page_config(
    page_title="Learning Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Learning Insights")

st.markdown(
"""
Identify concepts that require reinforcement based on audience performance.
"""
)

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""

SELECT

    q.question,

    AVG(r.score),

    COUNT(r.response_id)

FROM questions q

LEFT JOIN responses r

ON q.question_id = r.question_id

GROUP BY q.question

ORDER BY AVG(r.score) ASC

""")

results = cursor.fetchall()

conn.close()

weak = 0
moderate = 0
strong = 0

for _, avg, _ in results:

    avg = avg or 0

    if avg < 10:

        weak += 1

    elif avg < 15:

        moderate += 1

    else:

        strong += 1

c1,c2,c3 = st.columns(3)

with c1:

    st.metric(
        "Weak Concepts",
        weak
    )

with c2:

    st.metric(
        "Moderate Concepts",
        moderate
    )

with c3:

    st.metric(
        "Strong Concepts",
        strong
    )

st.divider()

for question,avg,responses in results:

    avg = avg or 0

    with st.container(border=True):

        st.markdown(
            f"### {question}"
        )

        st.metric(
            "Average Score",
            f"{avg:.1f}/20"
        )

        st.write(
            f"Responses : {responses}"
        )

        if avg >= 15:

            st.success(
                "Strong Understanding"
            )

            st.info(
                "Most participants demonstrated good understanding."
            )

        elif avg >= 10:

            st.warning(
                "Moderate Understanding"
            )

            st.info(
                "Some participants understood the concept, but improvement is possible."
            )

        else:

            st.error(
                "Weak Understanding"
            )

            st.warning(
                "This concept should be revisited in future sessions."
            )

st.divider()

st.subheader("🤖 AI Recommendations")

if weak == 0:

    st.success(
        """
Excellent session.

Participants understood almost every concept.

Recommendation:
Move towards more advanced topics.
"""
    )

elif weak <= 2:

    st.warning(
        """
A few concepts require reinforcement.

Recommendation:

• Spend more time explaining difficult concepts.

• Add one practical example before moving ahead.

• Conduct one revision quiz.
"""
    )

else:

    st.error(
        """
Audience struggled with multiple concepts.

Recommendation:

• Repeat the lecture.

• Use more real-world examples.

• Reduce question difficulty.

• Conduct another assessment after revision.
"""
    )

st.divider()

st.caption(
    "AudienceIQ Learning Insights"
)