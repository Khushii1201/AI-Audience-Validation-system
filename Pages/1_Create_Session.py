import streamlit as st

from utils.ui_styles import load_css

from database.db import create_tables

from database.session_repo import create_session

from database.question_repo import save_question

from database.question_bank_repo import (
    search_question_bank,
    get_question_bank,
    increase_usage,
    save_question_bank
)

from ai.question_generator import generate_questions

load_css()

create_tables()

st.set_page_config(
    page_title="Create Session",
    layout="wide"
)

st.title(" Create AI Session")

st.markdown("""
Create AI-powered learning sessions with reusable question banks.
""")

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Medium"

if "question_source" not in st.session_state:
    st.session_state.question_source = "AI"

if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = []

if "bank_results" not in st.session_state:
    st.session_state.bank_results = []

edited_questions = []

# ----------------------------------------------------
# Topic
# ----------------------------------------------------

topic = st.text_input(
    "📚 Session Topic",
    value=st.session_state.topic,
    placeholder="Example: Artificial Intelligence"
)

st.session_state.topic = topic

# ----------------------------------------------------
# Difficulty
# ----------------------------------------------------

difficulty = st.radio(
    " Difficulty",
    ["Easy", "Medium", "Hard"],
    horizontal=True,
    index=["Easy", "Medium", "Hard"].index(
        st.session_state.difficulty
    )
)

st.session_state.difficulty = difficulty

# ----------------------------------------------------
# Question Source
# ----------------------------------------------------

question_source = st.radio(
    "Question Source",
    [
        "AI",
        "Question Bank",
        "Hybrid"
    ],
    horizontal=True
)

st.session_state.question_source = question_source

st.divider()

# ----------------------------------------------------
# Search Question Bank
# ----------------------------------------------------

st.subheader("🔍 Search Previous Question Sets")

if st.button(
    "Search Previous Questions",
    use_container_width=True
):

    if topic.strip() == "":

        st.warning(
            "Please enter a topic."
        )

    else:

        st.session_state.bank_results = search_question_bank(
            topic,
            difficulty
        )
# ----------------------------------------------------
# Display Previous Question Sets
# ----------------------------------------------------

if len(st.session_state.bank_results) > 0:

    st.success(
        f"Found {len(st.session_state.bank_results)} previous question set(s)."
    )

    for (
        bank_id,
        topic_name,
        difficulty_name,
        questions_json,
        usage_count,
        created_at
    ) in st.session_state.bank_results:

        with st.container(border=True):

            left, right = st.columns([4, 1])

            with left:

                st.markdown(f"### 📘 {topic_name}")

                st.write(f"**Difficulty:** {difficulty_name}")
                st.write(f"**Used:** {usage_count} times")
                st.write(f"**Created:** {created_at}")

            with right:

                if st.button(
                    "Use",
                    key=f"use_bank_{bank_id}"
                ):

                    st.session_state.generated_questions = (
                        get_question_bank(bank_id)
                    )

                    increase_usage(bank_id)

                    st.success(
                        "Question set loaded successfully!"
                    )

st.divider()



st.subheader(" Generate Questions")

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
                "Generating questions..."
            ):

                # ---------------- AI ----------------

                if question_source == "AI":

                    st.session_state.generated_questions = (
                        generate_questions(
                            topic,
                            difficulty
                        )
                    )

                # ---------------- Question Bank ----------------

                elif question_source == "Question Bank":

                    if len(
                        st.session_state.bank_results
                    ) == 0:

                        st.warning(
                            "No previous question set found."
                        )

                    else:

                        st.info(
                            "Click 'Use' on a question set above."
                        )

                # ---------------- Hybrid ----------------

                elif question_source == "Hybrid":

                    ai_questions = generate_questions(
                        topic,
                        difficulty
                    )

                    previous_questions = []

                    if len(
                        st.session_state.bank_results
                    ) > 0:

                        previous_questions = get_question_bank(
                            st.session_state.bank_results[0][0]
                        )

                    hybrid = []

                    hybrid.extend(previous_questions[:2])

                    hybrid.extend(ai_questions[:3])

                    st.session_state.generated_questions = hybrid

                st.success(
                    "Questions generated successfully!"
                )

with col2:

    if st.button(
        " Regenerate",
        use_container_width=True
    ):

        if topic.strip() == "":

            st.warning(
                "Please enter a topic."
            )

        else:

            with st.spinner(
                "Generating a fresh set..."
            ):

                st.session_state.generated_questions = (
                    generate_questions(
                        topic,
                        difficulty
                    )
                )

                st.success(
                    "New question set generated."
                )

# ----------------------------------------------------
# Summary
# ----------------------------------------------------

if len(st.session_state.generated_questions) > 0:

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Questions",
            len(st.session_state.generated_questions)
        )

    with c2:

        st.metric(
            "Difficulty",
            difficulty
        )

    with c3:

        st.metric(
            "Source",
            question_source
        )

    st.progress(0.5)

    st.success(
        "Question generation completed."
    )
# ----------------------------------------------------
# Review Questions
# ----------------------------------------------------

if len(st.session_state.generated_questions) > 0:

    st.divider()

    st.subheader(" Review Questions")

    st.info(
        "Review, edit or delete questions before publishing."
    )

    edited_questions = []

    remove_index = None

    for i, q in enumerate(st.session_state.generated_questions):

        with st.expander(
            f"Question {i+1}",
            expanded=True
        ):

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

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{i}"
                ):

                    remove_index = i

            with col2:

                st.button(
                    " Regenerate",
                    key=f"regen_{i}",
                    disabled=True,
                    help="Coming soon"
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

    st.subheader("➕ Add Custom Question")

    custom_question = st.text_area(

        "New Question",

        key="custom_question"

    )

    custom_answer = st.text_area(

        "Expected Answer",

        key="custom_answer"

    )

    if st.button(

        "Add Question",

        use_container_width=True

    ):

        if (

            custom_question.strip()

            and

            custom_answer.strip()

        ):

            st.session_state.generated_questions.append(

                {

                    "question": custom_question,

                    "answer": custom_answer

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

# ----------------------------------------------------
# Final Question Count
# ----------------------------------------------------

    st.divider()

    st.metric(

        "Final Question Count",

        len(st.session_state.generated_questions)

    )

    if len(st.session_state.generated_questions) != 5:

        st.warning(

            "Recommended: Publish exactly 5 questions."

        )
# ----------------------------------------------------
# Publish Session
# ----------------------------------------------------

if len(st.session_state.generated_questions) > 0:

    st.divider()

    st.subheader(" Publish Session")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Publish Session",
            use_container_width=True,
            type="primary"
        ):

            with st.spinner(
                "Publishing Session..."
            ):

                # ---------------------------------
                # Create Session
                # ---------------------------------

                session_id = create_session(

                    st.session_state.topic,

                    st.session_state.difficulty

                )

                # ---------------------------------
                # Save Questions
                # ---------------------------------

                for q in edited_questions:

                    save_question(

                        session_id,

                        q["question"],

                        q["answer"]

                    )

                # ---------------------------------
                # Save Question Bank
                # ---------------------------------

                save_question_bank(

                    st.session_state.topic,

                    st.session_state.difficulty,

                    edited_questions

                )

                st.success(
                    "🎉 Session Published Successfully!"
                )

                st.balloons()

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

                st.subheader(
                    "Share With Audience"
                )

                st.code(
                    f"Session ID: {session_id}"
                )

                st.info(
                    """
Share this Session ID with your participants.

Participants can:

• Join the session

• Answer AI-generated questions

• Receive AI evaluation

• Appear on the leaderboard

• Contribute to analytics
"""
                )

    with col2:

        if st.button(
            " Clear Session",
            use_container_width=True
        ):

            st.session_state.generated_questions = []

            st.session_state.bank_results = []

            st.session_state.topic = ""

            st.session_state.difficulty = "Medium"

            st.session_state.question_source = "AI"

            st.success(
                "Session Cleared Successfully."
            )

            st.rerun()

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.divider()

st.caption(
    "AudienceIQ • AI-Powered Audience Validation Platform • Offline Mode (Ollama)"
)