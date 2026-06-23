import streamlit as st

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

from ai.ollama_evaluator import (
    evaluate_answer
)

create_tables()

st.set_page_config(
    page_title="Audience Portal",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Audience Portal")

st.markdown(
    """
    Welcome! Join the session and answer the questions.
    """
)

user_name = st.text_input(
    "👤 Your Name"
)

session_id = st.text_input(
    "🔑 Session ID"
)

if st.button(
    "Join Session"
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

    session_id = int(session_id)

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

if "questions" in st.session_state:

    st.divider()

    st.subheader(
        "📝 Questions"
    )

    answers = {}
    question_map = {}

    total_questions = len(
        st.session_state.questions
    )

    for index, (qid, question) in enumerate(
        st.session_state.questions,
        start=1
    ):

        question_map[qid] = question

        st.progress(
            index / total_questions
        )

        st.markdown(
            f"### Question {index}"
        )

        st.write(
            question
        )

        answers[qid] = st.text_area(
            "Your Answer",
            key=f"answer_{qid}"
        )

    st.divider()

    if st.button(
        "✅ Submit Answers"
    ):

        total_score = 0

        st.subheader(
            "📊 Evaluation Results"
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

                st.write(
                    f"Question ID: {qid}"
                )

                st.write(
                    f"Score: {score}/20"
                )

                st.write(
                    f"Feedback: {feedback}"
                )

        st.success(
            "🎉 Responses submitted successfully!"
        )

        st.metric(
            "Final Score",
            f"{total_score}/100"
        )

        st.balloons()