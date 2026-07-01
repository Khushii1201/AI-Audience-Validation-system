import streamlit as st

if st.session_state.get("role") != "speaker":

    st.error("Unauthorized Access")

    st.stop()
import ollama

from utils.ui_styles import load_css
from database.db import get_connection

load_css()

st.set_page_config(
    page_title="AI Insights",
    layout="wide"
)

st.title(" AI Insights")

st.markdown("""
AI-generated teaching recommendations based on audience performance.
""")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""

SELECT

    q.question,

    AVG(r.score)

FROM questions q

LEFT JOIN responses r

ON q.question_id = r.question_id

GROUP BY q.question

ORDER BY AVG(r.score)

""")

results = cursor.fetchall()

conn.close()

if len(results) == 0:

    st.info(
        "No session data available."
    )

    st.stop()
summary = ""

weak = []
strong = []

for question, score in results:

    score = score or 0

    summary += f"""

Question:
{question}

Average Score:
{score:.1f}/20

"""

    if score < 10:

        weak.append(question)

    elif score >= 15:

        strong.append(question)

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Weak Concepts",
        len(weak)
    )

with c2:

    st.metric(
        "Strong Concepts",
        len(strong)
    )

st.divider()
if st.button(
    "Generate AI Report",
    use_container_width=True
):

    with st.spinner(
        "Analysing audience performance..."
    ):

        prompt = f"""
You are an expert educator.

Below is the audience performance.

{summary}

Generate a report with these headings.

Overall Audience Understanding

Strong Concepts

Weak Concepts

Teaching Suggestions

Revision Plan

Difficulty Recommendation

Recommended Next Topic

Return only plain text.
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

        report = response["message"]["content"]

        st.success(
            "AI Report Generated Successfully."
        )

        st.markdown(report)

        st.download_button(

            "⬇ Download Report",

            report,

            file_name="AudienceIQ_AI_Report.txt"

        )

st.divider()

st.caption(
    "AudienceIQ • Offline AI Teaching Assistant"
)
