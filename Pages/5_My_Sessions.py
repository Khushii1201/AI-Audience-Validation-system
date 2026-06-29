import streamlit as st

from utils.ui_styles import load_css

from database.history_repo import (
    get_all_sessions,
    delete_session
)

load_css()

st.set_page_config(
    page_title="My Sessions",
    page_icon="📂",
    layout="wide"
)

st.title("📂 My Sessions")

st.markdown("""
View all previously created sessions and monitor their performance.
""")

sessions = get_all_sessions()

if len(sessions) == 0:

    st.info(
        "No sessions created yet."
    )

    st.stop()

st.success(
    f"{len(sessions)} Session(s) Found"
)

st.divider()
for (

    session_id,

    topic,

    difficulty,

    created_at,

    participants,

    average_score,

    highest_score,

    total_questions

) in sessions:

    with st.container(border=True):

        st.subheader(
            topic.title()
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Session ID",
                session_id
            )

        with c2:

            st.metric(
                "Difficulty",
                difficulty
            )

        with c3:

            st.metric(
                "Participants",
                participants
            )

        with c4:

            st.metric(
                "Questions",
                total_questions
            )

        c5, c6 = st.columns(2)

        with c5:

            st.metric(
                "Average Score",
                f"{average_score:.1f}"
            )

        with c6:

            st.metric(
                "Highest Score",
                highest_score
            )

        st.caption(
            f"Created : {created_at}"
        )

        st.divider()
        left, right = st.columns(2)

        with left:

            st.button(
                "📊 View Analytics",
                key=f"analytics_{session_id}",
                disabled=True,
                help="Coming Soon"
            )

        with right:

            if st.button(

                "🗑 Delete Session",

                key=f"delete_{session_id}"

            ):

                delete_session(
                    session_id
                )

                st.success(
                    "Session Deleted Successfully."
                )

                st.rerun()

st.divider()

st.caption(
    "AudienceIQ • Session History"
)