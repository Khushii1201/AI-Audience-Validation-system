import streamlit as st

from utils.ui_styles import load_css

load_css()

st.set_page_config(
    page_title="AudienceIQ",
    layout="wide"
)

st.title("AudienceIQ")

st.markdown("""
### AI-Powered Audience Validation Platform

Create learning sessions, evaluate participant responses using AI,
and analyze learning outcomes through detailed reports.
""")

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.info("""
Offline AI

Powered by Ollama
""")

with c2:

    st.info("""
Question Generation

Difficulty-based AI Questions
""")

with c3:

    st.info("""
Analytics

Learning Insights
""")

with c4:

    st.info("""
Evaluation

AI-based Response Scoring
""")

st.divider()

st.header("Project Features")

left, right = st.columns(2)

with left:

    st.markdown("""

### Speaker Features

- Create Sessions
- Select Difficulty
- Generate AI Questions
- Edit Questions
- Publish Session
- View Analytics
- Learning Insights
- AI Teaching Report

""")

with right:

    st.markdown("""

### Participant Features

- Join Session
- Answer Questions
- AI Evaluation
- Instant Feedback
- Final Score
- Leaderboard

""")
st.divider()

st.header("Workflow")

st.markdown("""

1. Create a learning session

2. Choose the difficulty level

3. Generate AI-based questions

4. Publish the session

5. Participants join using the Session ID

6. Participants answer the questions

7. AI evaluates every response

8. Analytics and Learning Insights are generated

9. View Leaderboard and AI Report

""")

st.divider()

st.header("Modules")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""

#### Available Pages

- Create Session

- Join Session

- Analytics

- Learning Insights

""")

with c2:

    st.markdown("""

#### Additional Pages

- My Sessions

- Leaderboard

- AI Insights

""")

st.divider()

st.header("System")

st.success(
    """
Application Status

• Offline Mode Enabled

• AI Model : Qwen2.5 3B

• Question Generation : Ollama

• AI Evaluation : Ollama

• Database : SQLite
"""
)

st.divider()

st.caption(
    "AudienceIQ - AI Powered Audience Validation Platform"
)
