import streamlit as st


def load_css():

    st.markdown("""

<style>

/* ---------------- Background ---------------- */

.stApp{

    background:#0f172a;

    color:white;

}

/* ---------------- Sidebar ---------------- */

section[data-testid="stSidebar"]{

    background:#111827;

    border-right:1px solid #374151;

}

/* ---------------- Titles ---------------- */

h1{

    color:white;

    font-weight:700;

}

h2{

    color:white;

}

h3{

    color:#d1d5db;

}

/* ---------------- Buttons ---------------- */

.stButton>button{

    background:#2563eb;

    color:white;

    border:none;

    border-radius:12px;

    padding:0.7rem;

    font-weight:600;

    transition:0.3s;

}

.stButton>button:hover{

    background:#1d4ed8;

    transform:translateY(-2px);

}

/* ---------------- Text Inputs ---------------- */

.stTextInput input{

    border-radius:10px;

    border:1px solid #374151;

    background:#1f2937;

    color:white;

}

/* ---------------- Text Areas ---------------- */

.stTextArea textarea{

    border-radius:10px;

    background:#1f2937;

    color:white;

}

/* ---------------- Selectbox ---------------- */

.stSelectbox{

    border-radius:10px;

}

/* ---------------- Radio ---------------- */

.stRadio{

    padding:10px;

}

/* ---------------- Metric Cards ---------------- */

[data-testid="metric-container"]{

    background:#1f2937;

    border-radius:15px;

    padding:20px;

    border:1px solid #374151;

}

/* ---------------- Containers ---------------- */

div[data-testid="stVerticalBlock"]>div:has(div.stContainer){

    border-radius:15px;

}

/* ---------------- Progress ---------------- */

.stProgress>div>div{

    background:#3b82f6;

}

/* ---------------- Success ---------------- */

.stSuccess{

    border-radius:10px;

}

/* ---------------- Warning ---------------- */

.stWarning{

    border-radius:10px;

}

/* ---------------- Error ---------------- */

.stError{

    border-radius:10px;

}

/* ---------------- Expander ---------------- */

.streamlit-expanderHeader{

    font-weight:600;

}

/* ---------------- Code Block ---------------- */

code{

    color:#38bdf8;

}

/* ---------------- Footer ---------------- */

footer{

    visibility:hidden;

}

#MainMenu{

    visibility:hidden;

}

header{

    visibility:hidden;

}

</style>

""", unsafe_allow_html=True)