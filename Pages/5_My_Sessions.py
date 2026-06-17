import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.history_repo import (
    get_all_sessions
)

st.set_page_config(
    page_title="My Sessions",
    layout="wide"
)

st.title(" My Sessions")

st.markdown("""
View all previously created sessions and their performance.
""")

sessions = get_all_sessions()

if len(sessions) == 0:

    st.info(
        "No sessions found."
    )

else:

    st.subheader(
        "Session History"
    )

    for (
        session_id,
        topic,
        participants,
        avg_score
    ) in sessions:

        if avg_score is None:

            avg_score = 0

        with st.container(
            border=True
        ):

            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:

                st.subheader(
                    topic
                )

                st.write(
                    f"Session ID: {session_id}"
                )

                st.write(
                    f"Participants: {participants}"
                )

            with col2:

                st.metric(
                    "Avg Score",
                    f"{avg_score:.1f}"
                )

            if avg_score >= 80:

                st.success(
                    "Excellent Audience Understanding"
                )

            elif avg_score >= 60:

                st.warning(
                    "Moderate Audience Understanding"
                )

            else:

                st.error(
                    "Learning Gaps Detected"
                )