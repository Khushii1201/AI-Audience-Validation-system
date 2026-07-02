import streamlit as st

st.set_page_config(
    page_title="AudienceIQ",
    layout="wide"
)

# -----------------------------------------
# Session State
# -----------------------------------------

if "role" not in st.session_state:
    st.session_state.role = None

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

SPEAKER_PASSWORD = "audienceiq123"

# -----------------------------------------
# Login Screen
# -----------------------------------------

if not st.session_state.authenticated:

    st.title("AudienceIQ")

    st.write(
        "Select the portal you want to access."
    )

    speaker, audience = st.columns(2)

    with speaker:

        st.subheader("Speaker Portal")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Enter Speaker Portal",
            use_container_width=True
        ):

            if password == SPEAKER_PASSWORD:

                st.session_state.role = "speaker"
                st.session_state.authenticated = True
                st.rerun()

            else:

                st.error(
                    "Incorrect password."
                )

    with audience:

        st.subheader("Audience Portal")

        if st.button(
            "Enter Audience Portal",
            use_container_width=True
        ):

            st.session_state.role = "audience"
            st.session_state.authenticated = True
            st.rerun()

    st.stop()
# ----------------------------------------------------
# Speaker Pages
# ----------------------------------------------------

speaker_pages = [

    st.Page(
        "Pages/1_Create_Session.py",
        title="Create Session"
    ),

    st.Page(
        "Pages/3_Analytics.py",
        title="Analytics"
    ),

    st.Page(
        "Pages/4_Learning_Insights.py",
        title="Learning Insights"
    ),

    st.Page(
        "Pages/5_My_Sessions.py",
        title="My Sessions"
    ),

    st.Page(
        "Pages/8_AI_Insights.py",
        title="AI Insights"
    )

]

# ----------------------------------------------------
# Audience Pages
# ----------------------------------------------------

audience_pages = [

    st.Page(
        "Pages/2_Join_Session.py",
        title="Join Session"
    ),

    st.Page(
        "Pages/6_Leaderboard.py",
        title="Leaderboard"
    )

]

# ----------------------------------------------------
# Navigation
# ----------------------------------------------------

if st.session_state.role == "speaker":

    pages = speaker_pages

else:

    pages = audience_pages

pg = st.navigation(pages)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.divider()

    st.write(
        f"Logged in as: **{st.session_state.role.title()}**"
    )

    if st.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.role = None
        st.session_state.authenticated = False

        st.rerun()

# ----------------------------------------------------
# Run Selected Page
# ----------------------------------------------------

pg.run()
