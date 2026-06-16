import streamlit as st
st.title("AUDIENCE FILE RUNNING")
from database.db import (
    create_tables,
    get_connection
)

from database.response_repo import save_response

from database.question_repo import (
    get_correct_answer
)

from ai.evaluator import (
    evaluate_answer
)

create_tables()

st.title(
    "Audience Portal"
)

user_name = st.text_input(
    "Your Name"
)

session_id = st.text_input(
    "Session ID"
)

if st.button(
    "Join Session"
):

    if not session_id.isdigit():

        st.error(
            "Enter valid Session ID"
        )

        st.stop()

    session_id = int(
        session_id
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        question_id,
        question
        FROM questions
        WHERE session_id=?
        """,
        (session_id,)
    )

    questions = cursor.fetchall()

    conn.close()

    if len(questions) == 0:

        st.error(
            "Session Not Found"
        )

    else:

        st.session_state.questions = (
            questions
        )

        st.session_state.session_id = (
            session_id
        )

        st.session_state.user_name = (
            user_name
        )

if "questions" in st.session_state:

    answers = {}

    for qid, question in (
        st.session_state.questions
    ):

        answers[qid] = st.text_input(
            question,
            key=f"q_{qid}"
        )

    if st.button("Submit Answers"):
        st.write("SUBMIT BUTTON CLICKED")

    total_score = 0


    for qid, answer in (
            answers.items()
        ):

            correct_answer = (
                get_correct_answer(
                    qid
                )
            )

            score = (
                evaluate_answer(
                    answer,
                    correct_answer
                )
            )

            total_score += score

            save_response(
                st.session_state.session_id,
                qid,
                st.session_state.user_name,
                answer,
                score
            )

    st.success(
            "Responses Saved"
        )

    st.info(
         f"Score: {total_score}"
        )