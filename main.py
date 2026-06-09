import streamlit as st

from ai.question_generator import generate_questions
from database.db import create_tables

create_tables()

st.set_page_config(
    page_title="AI Audience Validation System",
    layout="wide"
)

st.title("AI Audience Validation System")

topic = st.text_input(
    "Enter Topic"
)

if st.button("Generate Questions"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Generating Questions..."):

            questions = generate_questions(topic)

        st.subheader("Generated Questions")

        st.write(questions)