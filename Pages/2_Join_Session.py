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
    layout="wide"
)

st.title("Audience Portal")

st.markdown(
"""
Join the session using your name and the session ID provided by the host.
"""
)

# User Details

user_name = st.text_input(
    " Participant Name"
)

session_id = st.text_input(
    " Session ID"
)

if st.button(
    "Join Session",
    use_container_width=True
):

    if user_name.strip() == "":

        st.error(
            "Please enter your name."
        )

        st.stop()

    if not session_id.isdigit():

        st.error(
            "Invalid Session ID."
        )

        st.stop()

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        question_id,

        question

    FROM questions

    WHERE session_id=?

    ORDER BY question_id

    """,

    (int(session_id),)

    )

    questions = cursor.fetchall()

    conn.close()

    if len(questions)==0:

        st.error(
            "Session not found."
        )

    else:

        st.session_state.questions = questions
        st.session_state.session_id = int(session_id)
        st.session_state.user_name = user_name

        st.success(
            "Successfully joined session."
        )

# -------------------------------------------------------
# Questions
# -------------------------------------------------------

if "questions" in st.session_state:

    st.divider()

    st.subheader(" Answer the Questions")

    answers = {}

    total = len(
        st.session_state.questions
    )

    question_lookup = {}

    for i,(qid,question) in enumerate(

        st.session_state.questions,

        start=1

    ):

        question_lookup[qid]=question

        st.progress(
            i/total
        )

        with st.container(border=True):

            st.markdown(
                f"### Question {i}"
            )

            st.write(question)

            answers[qid]=st.text_area(

                "Your Answer",

                key=f"answer_{qid}",

                height=120

            )

    st.divider()

    if st.button(

        " Submit Answers",

        use_container_width=True

    ):

        total_score=0

        st.subheader(
            " Evaluation Results"
        )

        for qid,student_answer in answers.items():

            expected_answer=get_correct_answer(
                qid
            )

            score,feedback=evaluate_answer(

                question_lookup[qid],

                expected_answer,

                student_answer

            )

            total_score+=score

            save_response(

                st.session_state.session_id,

                qid,

                st.session_state.user_name,

                student_answer,

                score

            )

            with st.container(border=True):

                st.write(
                    f"### Question {qid}"
                )

                st.metric(

                    "Score",

                    f"{score}/20"

                )

                st.write(

                    "**Feedback**"

                )

                st.info(
                    feedback
                )

        st.divider()
        # Prevent score from exceeding limits
total_score = max(0, min(total_score, 100))

percentage = total_score

st.metric(
    "Final Score",
    f"{total_score}/100"
)

st.progress(
    percentage / 100
)
st.progress(
            percentage/100
        )

if percentage >= 90:

    st.success(
        " Outstanding Performance!"
    )

elif percentage >= 75:

    st.success(
        " Excellent Work!"
    )

elif percentage >= 60:

    st.info(
        " Good Job!"
    )

elif percentage >= 40:

    st.warning(
        " You understand the basics. More practice is recommended."
    )

else:

    st.error(
        " Consider revising the topic and trying again."
    )

st.balloons()