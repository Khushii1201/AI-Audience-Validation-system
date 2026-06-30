import streamlit as st

from utils.ui_styles import load_css

load_css()

st.set_page_config(
    page_title="InsightLens-AI",
    layout="wide"
)

st.title("InsightLens-AI")

st.markdown(
"""
### AI-Powered Audience Understanding Platform

Create  assessments, evaluate responses using  AI,
track learning outcomes and generate actionable teaching insights.
"""
)

st.divider()

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.success(
        """
### 

Offline AI

Powered by Ollama
"""
    )

with c2:

    st.info(
        """
### 📚

Question Bank

Reusable AI Question Sets
"""
    )

with c3:

    st.warning(
        """
### 

Analytics

Real-time Learning Insights
"""
    )

with c4:

    st.error(
        """
### 

Leaderboard

Track Top Performers
"""
    )

st.divider()

st.header(" Features")

c1,c2 = st.columns(2)

with c1:

    st.markdown("""
### Speaker can:

- Create AI Sessions
- Select Difficulty
- Reuse Question Bank
- Generate Questions
- Publish Session
- AI Teaching Insights
""")

with c2:

    st.markdown("""
###    Audience can:

- Join Session
- Submit Answers
- AI Evaluation
- Instant Feedback
- Leaderboard
- Performance Tracking
""")
st.divider()

st.header(" Navigation")

col1,col2,col3 = st.columns(3)

with col1:

    st.page_link(
        "Pages/1_Create_Session.py",
        label=" Create Session"
    )

    st.page_link(
        "Pages/2_Audience.py",
        label=" Join Session"
    )

with col2:

    st.page_link(
        "Pages/3_Analytics.py",
        label="Analytics"
    )

    st.page_link(
        "Pages/4_Learning_Insights.py",
        label=" Learning Insights"
    )

with col3:

    st.page_link(
        "Pages/5_Leaderboard.py",
        label=" Leaderboard"
    )

    st.page_link(
        "Pages/7_Question_Bank.py",
        label=" Question Bank"
    )

st.divider()

st.info(
"""
###  Current AI Model
Offline

Model: **Qwen2.5:3B**

Evaluation: Ollama

Question Generation: Ollama
"""
)

st.divider()

st.caption(
    "InsightLens-AI v2.0 • Offline AI Audience Validation Platform"
)