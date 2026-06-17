import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.analytics_repo import (
    get_leaderboard
)

st.set_page_config(
    page_title="Leaderboard",
    layout="wide"
)

st.title("Top Participants")

st.markdown("""
Recognizing the best performing participants based on their cumulative scores.
""")

results = get_leaderboard()

if len(results) == 0:

    st.info(
        "No participant data available."
    )

else:

    rank = 1

    for user, score in results:

        if rank == 1:

            medal = "🥇"

        elif rank == 2:

            medal = "🥈"

        elif rank == 3:

            medal = "🥉"

        else:

            medal = "🎯"

        with st.container(border=True):

            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:

                st.subheader(
                    f"{medal} Rank {rank}"
                )

                st.write(
                    f"Participant: {user}"
                )

            with col2:

                st.metric(
                    "Score",
                    score
                )

        rank += 1

st.divider()

st.success(
    "Leaderboard updates automatically when new responses are submitted."
)