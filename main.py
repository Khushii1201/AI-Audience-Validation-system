import streamlit as st

from database.db import create_tables

from database.session_repo import create_session

from database.question_repo import save_question

from ai.question_generator import generate_questions

create_tables()

st.title(
    "AI Audience Validation System"
)

topic = st.text_input(
    "Enter Topic"
)

if st.button(
    "Generate Questions"
):

    if topic.strip() == "":

        st.error(
            "Please enter a topic"
        )

    else:

        session_id = create_session(
            topic
        )

        questions = generate_questions(
            topic
        )

        st.success(
            f"Session Created: {session_id}"
        )

        for q in questions:

            save_question(
                session_id,
                q["question"],
                q["answer"]
            )

            st.write(
                q["question"]
            )