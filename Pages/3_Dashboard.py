import streamlit as st

from database.analytics_repo import (
    get_total_responses,
    get_average_score,
    get_participant_scores
)

st.title(
    "Audience Understanding Dashboard"
)

st.subheader(
    "Participant Scores"
)

participants = get_participant_scores()

for user, score in participants:

    st.write(
        f"{user} : {score}"
    )

st.metric(
    "Total Responses",
    get_total_responses()
)

st.metric(
    "Average Score",
    f"{get_average_score():.2f}"
)

st.metric(
    "Clarity Score",
    f"{get_average_score():.2f}%"
)