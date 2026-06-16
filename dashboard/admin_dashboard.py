import streamlit as st

st.title(
    "Admin Dashboard"
)

st.page_link(
    "dashboard/dashboard.py",
    label="Analytics"
)

st.page_link(
    "dashboard/leaderboard.py",
    label="Leaderboard"
)

st.page_link(
    "dashboard/weak_areas.py",
    label="Weak Areas"
)

st.page_link(
    "dashboard/session_history.py",
    label="Session History"
)

st.page_link(
    "dashboard/question_analysis.py",
    label="Question Analysis"
)

st.page_link(
    "dashboard/charts.py",
    label="Charts"
)