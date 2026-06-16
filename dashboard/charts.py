import streamlit as st
import pandas as pd
import plotly.express as px

from database.analytics_repo import (
    get_participant_scores
)

st.title(
    "Performance Charts"
)

data = get_participant_scores()

df = pd.DataFrame(
    data,
    columns=[
        "User",
        "Score"
    ]
)

fig = px.bar(
    df,
    x="User",
    y="Score",
    title="Participant Scores"
)

st.plotly_chart(
    fig,
    use_container_width=True
)