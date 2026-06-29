import streamlit as st

from utils.ui_styles import load_css

from database.analytics_repo import (
    get_leaderboard
)

load_css()

st.set_page_config(
    page_title="Leaderboard",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Leaderboard")

st.markdown("""
Recognizing the best performing participants based on their cumulative scores.
""")

leaderboard = get_leaderboard()

if len(leaderboard) == 0:

    st.info(
        "No participants available."
    )

    st.stop()
for rank, (user, score) in enumerate(

    leaderboard,

    start=1

):

    if rank == 1:

        medal = "🥇"

        title = "Gold"

    elif rank == 2:

        medal = "🥈"

        title = "Silver"

    elif rank == 3:

        medal = "🥉"

        title = "Bronze"

    else:

        medal = "🏅"

        title = "Participant"

    with st.container(border=True):

        left, right = st.columns([4,1])

        with left:

            st.subheader(
                f"{medal} Rank {rank}"
            )

            st.write(
                f"Participant : **{user}**"
            )

            st.write(
                f"Badge : **{title}**"
            )

        with right:

            st.metric(

                "Score",

                score

            )

        progress = min(score/100,1)

        st.progress(progress)
        if score >= 90:

            st.success(
                "Outstanding Performance ⭐⭐⭐⭐⭐"
            )

        elif score >= 75:

            st.success(
                "Excellent Performance ⭐⭐⭐⭐"
            )

        elif score >= 60:

            st.info(
                "Good Performance ⭐⭐⭐"
            )

        elif score >= 40:

            st.warning(
                "Average Performance ⭐⭐"
            )

        else:

            st.error(
                "Needs Improvement ⭐"
            )

st.divider()

st.subheader("🏅 Achievement Levels")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.success(
        """
### 🥇 Gold

90+
"""
    )

with c2:

    st.info(
        """
### 🥈 Silver

75+
"""
    )

with c3:

    st.warning(
        """
### 🥉 Bronze

60+
"""
    )

with c4:

    st.error(
        """
### ⭐ Beginner

Below 60
"""
    )

st.divider()

st.caption(
    "Leaderboard updates automatically when new responses are submitted."
)