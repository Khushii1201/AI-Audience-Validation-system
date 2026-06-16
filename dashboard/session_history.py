import streamlit as st

from database.history_repo import (
    get_all_sessions
)

st.title(
    "Session History"
)

sessions = get_all_sessions()

for session_id, topic in sessions:

    st.write(
        f"Session {session_id} : {topic}"
    )