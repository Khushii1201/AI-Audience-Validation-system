import streamlit as st

from database.analytics_repo import (
    get_leaderboard
)

st.title(
    "Leaderboard"
)

results = get_leaderboard()

rank = 1

for user, score in results:

    st.write(
        f"{rank}. {user} - {score}"
    )

    rank += 1