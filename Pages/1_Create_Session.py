import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.db import create_tables
from database.session_repo import create_session
from database.question_repo import save_question
from ai.question_generator import generate_questions

create_tables()

st.set_page_config(
    page_title="Create Session",
    layout="wide"
)

st.title("Create Session")

st.markdown("""
Create an AI-powered learning session for your audience.
Generate questions, review them and publish the session.
""")

# -----------------------------
# Session State
# -----------------------------

if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = []

if "topic" not in st.session_state:
    st.session_state.topic = ""

# -----------------------------
# Topic Input
# -----------------------------

topic = st.text_input(
    "Enter Session Topic",
    value=st.session_state.topic,
    placeholder="Example: DBMS, Machine Learning, Operating Systems"
)

col1, col2 = st.columns(2)

# -----------------------------
# Generate Questions
# -----------------------------

with col1:

    if st.button(
        "Generate Questions",
        use_container_width=True
    ):

        if topic.strip() == "":

            st.warning(
                "Please enter a topic."
            )

        else:

            with st.spinner(
                "Generating AI Questions..."
            ):

                st.session_state.topic = topic

                st.session_state.generated_questions = (
                    generate_questions(topic)
                )

# -----------------------------
# Regenerate
# -----------------------------

with col2:

    if st.button(
        "Regenerate Questions",
        use_container_width=True
    ):

        if topic.strip() != "":

            with st.spinner(
                "Generating New Questions..."
            ):

                st.session_state.generated_questions = (
                    generate_questions(topic)
                )
                st.session_state.generated_questions = (
                    generate_questions(topic)
                    )
                st.write("DEBUG OUTPUT")
                st.write(st.session_state.generated_questions)
# -----------------------------
# Question Review
# -----------------------------

if len(st.session_state.generated_questions) > 0:

    st.progress(60)

    st.divider()

    st.subheader(" Review Questions")

    st.info(
        "Edit questions and answers before publishing."
    )

    edited_questions = []

    for i, q in enumerate(
        st.session_state.generated_questions
    ):

        with st.container(border=True):

            st.markdown(
                f"### Question {i+1}"
            )

            question = st.text_area(
                "Question",
                value=q["question"],
                key=f"question_{i}"
            )

            answer = st.text_area(
                "Expected Answer",
                value=q["answer"],
                key=f"answer_{i}"
            )

            edited_questions.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    st.divider()

    # -----------------------------
    # Publish Session
    # -----------------------------

    if st.button(
        " Publish Session",
        use_container_width=True
    ):

        session_id = create_session(
            st.session_state.topic
        )

        for q in edited_questions:

            save_question(
                session_id,
                q["question"],
                q["answer"]
            )

        st.progress(100)

        st.success(
            "Session Published Successfully!"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Session ID",
                session_id
            )

        with col2:

            st.metric(
                "Questions",
                len(edited_questions)
            )

        st.divider()

        st.subheader(" Share Session")

        st.code(
            f"Session ID: {session_id}"
        )

        st.info(
            "Share the Session ID with participants.They can now join and submit responses."
        )

        