import streamlit as st

from utils.ui_styles import load_css

from database.db import create_tables

from database.session_repo import create_session

from database.question_repo import save_question

from ai.question_generator import generate_questions

load_css()

create_tables()

st.set_page_config(
    page_title="Create Session",
    layout="wide"
)

st.title("Create Session")

st.write(
    "Create an AI-powered learning session."
)

# ------------------------------------
# Session State
# ------------------------------------

if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = []

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Medium"

edited_questions = []

# ------------------------------------
# Topic
# ------------------------------------

topic = st.text_input(
    "Session Topic",
    value=st.session_state.topic,
    placeholder="Example: Artificial Intelligence"
)

st.session_state.topic = topic

# ------------------------------------
# Difficulty
# ------------------------------------

difficulty = st.radio(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ],
    horizontal=True,
    index=[
        "Easy",
        "Medium",
        "Hard"
    ].index(
        st.session_state.difficulty
    )
)

st.session_state.difficulty = difficulty

st.divider()

col1, col2 = st.columns(2)

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
                "Generating Questions..."
            ):

                st.session_state.generated_questions = (
                    generate_questions(
                        topic,
                        difficulty
                    )
                )

                st.success(
                    "Questions Generated."
                )

with col2:

    if st.button(
        "Regenerate",
        use_container_width=True
    ):

        if topic.strip() != "":

            with st.spinner(
                "Generating New Questions..."
            ):

                st.session_state.generated_questions = (
                    generate_questions(
                        topic,
                        difficulty
                    )
                )

                st.success(
                    "New Questions Generated."
                )
# ----------------------------------------------------
# Review Questions
# ----------------------------------------------------

if len(st.session_state.generated_questions) > 0:

    st.divider()

    st.subheader("Review Questions")

    st.write(
        "Review and edit the generated questions before publishing."
    )

    edited_questions = []

    remove_index = None

    for i, q in enumerate(
        st.session_state.generated_questions
    ):

        with st.container(border=True):

            st.markdown(
                f"### Question {i + 1}"
            )

            question = st.text_area(
                "Question",
                value=q["question"],
                key=f"question_{i}",
                height=90
            )

            answer = st.text_area(
                "Expected Answer",
                value=q["answer"],
                key=f"answer_{i}",
                height=90
            )

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "Delete",
                    key=f"delete_{i}"
                ):

                    remove_index = i

            with c2:

                st.button(
                    "Regenerate This Question",
                    key=f"regen_{i}",
                    disabled=True
                )

            edited_questions.append(
                {
                    "question": question,
                    "answer": answer
                }
            )

    if remove_index is not None:

        st.session_state.generated_questions.pop(
            remove_index
        )

        st.rerun()

    st.divider()

    st.subheader("Add Custom Question")

    new_question = st.text_area(
        "New Question",
        key="new_question"
    )

    new_answer = st.text_area(
        "Expected Answer",
        key="new_answer"
    )

    if st.button(
        "Add Question",
        use_container_width=True
    ):

        if new_question.strip() and new_answer.strip():

            st.session_state.generated_questions.append(
                {
                    "question": new_question,
                    "answer": new_answer
                }
            )

            st.success(
                "Question Added Successfully."
            )

            st.rerun()

        else:

            st.warning(
                "Please enter both question and answer."
            )

    st.divider()

    st.metric(
        "Total Questions",
        len(st.session_state.generated_questions)
    )
# ----------------------------------------------------
# Publish Session
# ----------------------------------------------------

    st.divider()

    if st.button(
        "Publish Session",
        use_container_width=True,
        type="primary"
    ):

        if len(edited_questions) == 0:

            st.warning(
                "Please generate at least one question."
            )

        else:

            with st.spinner(
                "Publishing Session..."
            ):

                session_id = create_session(

                    st.session_state.topic,

                    st.session_state.difficulty

                )

                for q in edited_questions:

                    save_question(

                        session_id,

                        q["question"],

                        q["answer"]

                    )

                st.success(
                    "Session Published Successfully."
                )

                st.divider()

                c1, c2, c3 = st.columns(3)

                with c1:

                    st.metric(
                        "Session ID",
                        session_id
                    )

                with c2:

                    st.metric(
                        "Questions",
                        len(edited_questions)
                    )

                with c3:

                    st.metric(
                        "Difficulty",
                        st.session_state.difficulty
                    )

                st.divider()

                st.subheader("Share Session")

                st.code(
                    f"Session ID: {session_id}"
                )

                st.info(
                    """
Share the Session ID with participants.

Participants can join the session,
answer the questions and receive
AI-generated evaluation instantly.
"""
                )

# ----------------------------------------------------
# Clear Session
# ----------------------------------------------------

    if st.button(
        "Clear Session",
        use_container_width=True
    ):

        st.session_state.generated_questions = []

        st.session_state.topic = ""

        st.session_state.difficulty = "Medium"

        st.success(
            "Session Cleared."
        )

        st.rerun()

st.divider()

st.caption(
    "AudienceIQ - AI Powered Audience Validation Platform"
)
