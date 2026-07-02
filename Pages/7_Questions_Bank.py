import streamlit as st
from utils.ui_styles import load_css

from database.question_bank_repo import (

    get_all_question_banks,

    get_question_bank,

    increase_usage,

    delete_question_bank

)

load_css()

st.set_page_config(

    page_title="Question Bank",
    layout="wide"

)

st.title("Question Bank")

st.markdown(
"""
Browse previously generated AI question sets.
Reuse them instantly.
"""
)

search = st.text_input(
    " Search Topic"
)

difficulty = st.selectbox(

    "Difficulty",

    [

        "All",

        "Easy",

        "Medium",

        "Hard"

    ]

)

question_sets = get_all_question_banks()

filtered = []
for (

    bank_id,

    topic,

    diff,

    questions_json,

    usage,

    created_at

) in question_sets:

    if search:

        if search.lower() not in topic.lower():

            continue

    if difficulty != "All":

        if diff != difficulty:

            continue

    filtered.append(

        (

            bank_id,

            topic,

            diff,

            questions_json,

            usage,

            created_at

        )

    )

st.success(

    f"{len(filtered)} Question Set(s)"

)

st.divider()
for (

    bank_id,

    topic,

    diff,

    questions_json,

    usage,

    created_at

) in filtered:

    with st.container(border=True):

        st.subheader(
            topic.title()
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Difficulty",
                diff
            )

        with c2:

            st.metric(
                "Usage",
                usage
            )

        with c3:

            st.metric(
                "Bank ID",
                bank_id
            )

        st.caption(
            f"Created : {created_at}"
        )

        questions = get_question_bank(
            bank_id
        )

        for i, q in enumerate(

            questions,

            start=1

        ):

            with st.expander(

                f"Question {i}"

            ):

                st.write(
                    q["question"]
                )

                st.success(
                    q["answer"]
                )

        left, right = st.columns(2)

        with left:

            if st.button(

                "♻ Use",

                key=f"use_{bank_id}"

            ):

                increase_usage(
                    bank_id
                )

                st.session_state.generated_questions = questions

                st.success(
                    "Question Set Loaded."
                )

        with right:

            if st.button(

                "🗑 Delete",

                key=f"delete_{bank_id}"

            ):

                delete_question_bank(
                    bank_id
                )

                st.success(
                    "Question Set Deleted."
                )

                st.rerun()

st.divider()

st.caption(
    "AudienceIQ Question Repository"
)