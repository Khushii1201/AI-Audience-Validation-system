import streamlit as st

from database.db import create_tables
from database.session_repo import create_session
from database.question_repo import save_question
from ai.question_generator import generate_questions

create_tables()

st.title("Speaker Module")

st.markdown(
    """
    Create a session and generate audience validation questions.
    """
)

topic = st.text_input(
    "Enter Topic"
)

if st.button("Generate Questions"):

    if topic.strip() == "":

        st.warning(
            "Please enter a topic."
        )

    else:

        session_id = create_session(
            topic
        )

        questions = generate_questions(
            topic
        )

        st.success(
            f"Session Created Successfully! Session ID: {session_id}"
        )

        st.subheader(
            "Generated Questions"
        )

        for index, q in enumerate(
            questions,
            start=1
        ):

            save_question(
                session_id,
                q["question"],
                q["answer"]
            )

            with st.expander(
                f"Question {index}"
            ):

                st.write(
                    f" {q['question']}"
                )

                st.write(
                    f" Expected Answer: {q['answer']}"
                )

        st.info(
            f"Share Session ID {session_id} with participants."
        )