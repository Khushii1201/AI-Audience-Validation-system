import streamlit as st

st.set_page_config(
    page_title="Audience Portal",
    layout="wide"
)

join = st.Page(
    "Pages/2_Join_Session.py",
    title="Join Session",
    icon=":material/login:"
)

leaderboard = st.Page(
    "Pages/6_Leaderboard.py",
    title="Leaderboard",
    icon=":material/leaderboard:"
)

pg = st.navigation(
    [
        join,
        leaderboard
    ]
)

pg.run()