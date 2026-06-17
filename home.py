import streamlit as st

st.set_page_config(
    page_title="InsightLens: An AI-Audience Validation System",
    layout="wide"
)

# ---------- HERO ----------

st.markdown("""
<div style="
background:#1E293B;
padding:35px;
border-radius:20px;
text-align:center;
">

<h1 style="
color:#60A5FA;
">
InsightLens-AI
</h1>

<h3 style="
color:#D1D5DB;
">
Measure Your Audience Understanding in Real Time
</h3>

<p style="
color:#CBD5E1;
font-size:18px;
">
Generate AI questions, evaluate audience responses,
identify learning gaps and gain actionable insights ,All at one platform.
</p>

</div>
""",
unsafe_allow_html=True)

st.divider()

# ---------- FEATURES ----------

st.subheader("Our Platform Features:--")

c1, c2, c3 = st.columns(3)

with c1:

    with st.container(border=True):

        st.markdown("""
        ### Create Session

        ->Generate AI-powered questions
                    
        ->Review and approve questions
                    
        ->Publish learning sessions
        """)

with c2:

    with st.container(border=True):

        st.markdown("""
        ### Audience Participation

        ->Join sessions
                    
        ->Submit responses
                    
        ->Receive instant evaluation
        """)

with c3:

    with st.container(border=True):

        st.markdown("""
        ### Analytics & Insights

        ->Learning analytics
                    
        ->Weak area detection
                    
        ->Audience understanding metrics
        """)

st.divider()

# ---------- MODULES ----------

st.subheader("Available Modules")

col1, col2, col3 = st.columns(3)

with col1:

    st.success(" Create Session")

    st.success(" Join Session")

with col2:

    st.success("Analytics")

    st.success(" Learning Insights")

with col3:

    st.success("Leaderboard")

    st.success(" My Sessions")

st.divider()
