import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.db import get_connection

from google import genai
from dotenv import load_dotenv

import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.set_page_config(
    page_title="AI Insights",
    layout="wide"
)

st.title("AI Insights")

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT
q.question,
AVG(r.score)
FROM responses r
JOIN questions q
ON r.question_id=q.question_id
GROUP BY q.question
""")

results = cursor.fetchall()

conn.close()

if len(results) == 0:

    st.info(
        "No response data available."
    )

    st.stop()

# --------------------
# Build AI Prompt
# --------------------

analysis_text = ""

for question, score in results:

    analysis_text += (
        f"\nQuestion: {question}"
        f"\nAverage Score: {score:.1f}/20\n"
    )

prompt = f"""
You are an educational analytics expert.

Analyze the following audience performance data.

{analysis_text}

Provide:

1. Weakest concepts
2. Strongest concepts
3. Learning gaps
4. Suggested revision topics
5. Overall audience understanding

Keep response professional.
"""

with st.spinner(
    "Generating AI Insights..."
):

    response = (
        client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
    )

st.markdown(
    response.text
)