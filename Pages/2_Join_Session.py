import streamlit as st
from utils.ui_styles import load_css

load_css()

from database.db import (
    create_tables,
    get_connection
)

from database.response_repo import (
    save_response
)

from database.question_repo import (
    get_correct_answer
)

from ai.groq_evaluator import (
    evaluate_answer
)

create_tables()

st.set_page_config(
    page_title="Join Session",
    layout="wide"
)

st.title("Join Session")


st.divider()

# -----------------------------
# JOIN SESSION
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    user_name = st.text_input(
        "Enter Your Name"
    )

with col2:

    session_id = st.text_input(
        " Session ID"
    )

if st.button(
    " Join Session",
    use_container_width=True
):

    if user_name.strip() == "":

        st.error(
            "Please enter your name."
        )

        st.stop()

    if not session_id.isdigit():

        st.error(
            "Please enter a valid Session ID."
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
        WHERE session_id = ?
        """,
        (session_id,)
    )

    questions = cursor.fetchall()

    conn.close()

    if len(questions) == 0:

        st.error(
            "Session not found."
        )

    else:

        st.session_state.questions = questions
        st.session_state.session_id = session_id
        st.session_state.user_name = user_name

        st.success(
            "Successfully joined session."
        )

# -----------------------------
# DISPLAY QUESTIONS
# -----------------------------

if "questions" in st.session_state:

    st.divider()

    total_questions = len(
        st.session_state.questions
    )

    st.subheader(
        " Questions:"
    )

    st.info(
        f"Total Questions: {total_questions}"
    )

    answers = {}

    question_map = {}

    for index, (
            qid,
            question
    ) in enumerate(
        st.session_state.questions,
        start=1
    ):

        question_map[qid] = question

        st.progress(
            index / total_questions
        )

        with st.container(
            border=True
        ):

            st.markdown(
                f"### Question {index} of {total_questions}"
            )

            st.write(
                question
            )

            answers[qid] = st.text_area(
                "Your Answer",
                key=f"answer_{qid}",
                height=120
            )

    st.divider()

    # -----------------------------
    # SUBMIT
    # -----------------------------

    if st.button(
        "Submit Assessment",
        use_container_width=True
    ):

        total_score = 0

        st.subheader(
            "Evaluation Results"
        )

        for qid, answer in answers.items():

            correct_answer = (
                get_correct_answer(
                    qid
                )
            )

            score, feedback = (
                evaluate_answer(
                    question_map[qid],
                    correct_answer,
                    answer
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

            with st.container(
                border=True
            ):

                st.metric(
                    "Question Score",
                    f"{score}/20"
                )

                st.write(
                    f" Feedback: {feedback}"
                )

        st.divider()

        st.metric(
            "Final Score",
            f"{total_score}/100"
        )

        if total_score >= 80:

            st.success(
                "Excellent understanding of the topic."
            )

        elif total_score >= 60:

            st.warning(
                "Good understanding. Some concepts need reinforcement."
            )

        else:

            st.error(
                "Learning gaps detected. Additional revision is recommended."
            )

        st.balloons()

        st.success(
            "Assessment submitted successfully."
        )