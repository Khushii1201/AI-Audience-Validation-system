import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main {
        background-color: #0E1117;
    }

    .stButton > button {

        background-color: #2563EB;

        color: white;

        border-radius: 12px;

        border: none;

        font-weight: 600;

        height: 3em;

        width: 100%;
    }

    .stButton > button:hover {

        background-color: #3B82F6;

        color: white;
    }

    [data-testid="stMetric"] {

        background-color: #1E293B;

        border-radius: 16px;

        padding: 15px;

        border: 1px solid #334155;
    }

    .stTextInput input {

        border-radius: 10px;
    }

    .stTextArea textarea {

        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)