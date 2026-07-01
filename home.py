import streamlit as st

if st.session_state.get("role") != "speaker":

    st.error("Unauthorized Access")

    st.stop()
st.set_page_config(
    page_title="AudienceIQ - Speaker Portal",
    layout="wide"
)

create = st.Page(
    "Pages/1_Create_Session.py",
    title="Create Session",
    icon=":material/add_circle:"
)

analytics = st.Page(
    "Pages/3_Analytics.py",
    title="Analytics",
    icon=":material/analytics:"
)

learning = st.Page(
    "Pages/4_Learning_Insights.py",
    title="Learning Insights",
    icon=":material/school:"
)

sessions = st.Page(
    "Pages/5_My_Sessions.py",
    title="My Sessions",
    icon=":material/folder:"
)

ai = st.Page(
    "Pages/8_AI_Insights.py",
    title="AI Insights",
    icon=":material/psychology:"
)

pg = st.navigation(
    [
        create,
        analytics,
        learning,
        sessions,
        ai
    ]
)

pg.run()