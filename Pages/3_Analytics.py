import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.analytics_repo import (
    get_total_responses,
    get_average_score,
    get_participant_scores
)
from utils.export_excel import (
    export_results
)

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

st.title(" Analytics Dashboard")

# ----------------------------------
# Data
# ----------------------------------

participants = get_participant_scores()

response_count = get_total_responses()

average_score = get_average_score()

highest_score = 0

participant_count = len(participants)

if participants:

    highest_score = max(
        score
        for _, score in participants
    )

# ----------------------------------
# KPI CARDS
# ----------------------------------

st.subheader(
    "Session Overview"
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Responses",
        response_count
    )

with col2:

    st.metric(
        "Participants",
        participant_count
    )

with col3:

    st.metric(
        "Average Score",
        f"{average_score:.1f}"
    )

with col4:

    st.metric(
        "Highest Score",
        highest_score
    )

st.divider()

# ----------------------------------
# UNDERSTANDING LEVEL
# ----------------------------------

st.subheader(
    "Audience Understanding: how well the audience grasped the topic"
)

if average_score >= 80:

    st.success(
        """
        Excellent Understanding

        Most participants have a strong grasp of the topic.
        """
    )

elif average_score >= 60:

    st.warning(
        """
        Moderate Understanding

        Some concepts may require reinforcement.
        """
    )

else:

    st.error(
        """
        Learning Gaps Detected

        Significant revision is recommended.
        """
    )

st.divider()

# ----------------------------------
# TOP PERFORMERS
# ----------------------------------

st.subheader(
    "🏆 Top Participants"
)

if len(participants) == 0:

    st.info(
        "No participant data available."
    )

else:

    rank = 1

    for user, score in participants:

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
                [4,1]
            )

            with col1:

                st.write(
                    f"{medal} {user}"
                )

            with col2:

                st.write(
                    f"{score}"
                )

        rank += 1

st.divider()

# ----------------------------------
# PERFORMANCE DISTRIBUTION
# ----------------------------------

st.subheader(
    "📊 Performance Distribution"
)

excellent = 0
good = 0
needs_help = 0

for _, score in participants:

    if score >= 80:

        excellent += 1

    elif score >= 60:

        good += 1

    else:

        needs_help += 1

c1, c2, c3 = st.columns(3)

with c1:

    st.success(
        f"Excellent: {excellent}"
    )

with c2:

    st.warning(
        f"Good: {good}"
    )

with c3:

    st.error(
        f"Needs Help: {needs_help}"
    )

st.divider()

# ----------------------------------
# SESSION SUMMARY
# ----------------------------------

st.subheader(
    "📋 Session Summary"
)

st.info(
    f"""
    Total Participants: {participant_count}

    Total Responses: {response_count}

    Average Score: {average_score:.1f}

    Highest Score: {highest_score}
    """
)
st.divider()

if st.button(
    "📥 Export Results"
):

    filename = (
        export_results()
    )

    with open(
        filename,
        "rb"
    ) as file:

        st.download_button(
            label="Download Excel File",
            data=file,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )