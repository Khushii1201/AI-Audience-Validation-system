import streamlit as st

st.set_page_config(
    page_title="AI Audience Validation System",
    page_icon="🎯",
    layout="wide"
)

st.title(
    "🎯 AI Audience Validation System"
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Speaker",
        "Audience",
        "Dashboard",
        "Leaderboard",
        "Weak Areas",
        "Session History"
    ]
)

if page == "Speaker":

    st.header(
        "Speaker Module"
    )

    st.info(
        "Generate questions for a session"
    )

elif page == "Audience":

    st.header(
        "Audience Module"
    )

elif page == "Dashboard":

    st.header(
        "Analytics Dashboard"
    )

elif page == "Leaderboard":

    st.header(
        "Leaderboard"
    )

elif page == "Weak Areas":

    st.header(
        "Weak Area Detection"
    )

elif page == "Session History":

    st.header(
        "Session History"
    )