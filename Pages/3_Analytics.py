import streamlit as st

from database.analytics_repo import (

    get_total_responses,
    get_total_participants,
    get_average_score,
    get_highest_score,
    get_lowest_score,
    get_leaderboard,
    get_performance_distribution,
    get_topic_statistics,
    get_difficulty_statistics,
    get_question_bank_usage

)

st.set_page_config(

    page_title="Analytics Dashboard",

    page_icon="📊",

    layout="wide"

)

st.title("📊 Analytics Dashboard")

st.markdown(
"""
Monitor audience understanding and session performance.
"""
)

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------

responses = get_total_responses()

participants = get_total_participants()

average = get_average_score()

highest = get_highest_score()

lowest = get_lowest_score()

c1,c2,c3,c4,c5 = st.columns(5)

with c1:

    st.metric(
        "Responses",
        responses
    )

with c2:

    st.metric(
        "Participants",
        participants
    )

with c3:

    st.metric(
        "Average",
        average
    )

with c4:

    st.metric(
        "Highest",
        highest
    )

with c5:

    st.metric(
        "Lowest",
        lowest
    )

st.divider()

# -------------------------------------------------------
# Leaderboard
# -------------------------------------------------------

st.subheader("🏆 Top Participants")

leaderboard = get_leaderboard()

for i,(user,score) in enumerate(
    leaderboard[:5],
    start=1
):

    medal=""

    if i==1:

        medal="🥇"

    elif i==2:

        medal="🥈"

    elif i==3:

        medal="🥉"

    else:

        medal="🏅"

    st.write(
        f"{medal} {user} — {score}/100"
    )

st.divider()

# -------------------------------------------------------
# Performance Distribution
# -------------------------------------------------------

st.subheader("📈 Performance Distribution")

distribution = get_performance_distribution()

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Excellent",
        distribution["Excellent"]
    )

with c2:

    st.metric(
        "Good",
        distribution["Good"]
    )

with c3:

    st.metric(
        "Average",
        distribution["Average"]
    )

with c4:

    st.metric(
        "Needs Help",
        distribution["Needs Help"]
    )

st.divider()

# -------------------------------------------------------
# Topic Analytics
# -------------------------------------------------------

st.subheader("📚 Topic Analytics")

topics = get_topic_statistics()

if len(topics)==0:

    st.info(
        "No topic analytics available."
    )

else:

    for topic,avg,participants in topics:

        with st.container(border=True):

            st.markdown(
                f"### {topic}"
            )

            c1,c2 = st.columns(2)

            with c1:

                st.metric(
                    "Average Score",
                    f"{avg:.2f}"
                )

            with c2:

                st.metric(
                    "Participants",
                    participants
                )

st.divider()

# -------------------------------------------------------
# Difficulty Analytics
# -------------------------------------------------------

st.subheader("🎯 Difficulty Analytics")

difficulty = get_difficulty_statistics()

if len(difficulty)==0:

    st.info(
        "No difficulty statistics."
    )

else:

    cols = st.columns(
        len(difficulty)
    )

    for i,(level,avg) in enumerate(
        difficulty
    ):

        with cols[i]:

            st.metric(

                level,

                f"{avg:.2f}"

            )

st.divider()

# -------------------------------------------------------
# Question Bank Usage
# -------------------------------------------------------

st.subheader("📚 Most Reused Question Sets")

usage = get_question_bank_usage()

if len(usage)==0:

    st.info(
        "Question bank is empty."
    )

else:

    for topic,difficulty,used in usage:

        with st.container(border=True):

            st.markdown(
                f"### {topic}"
            )

            st.write(
                f"Difficulty : {difficulty}"
            )

            st.write(
                f"Used : {used} times"
            )

st.divider()

# -------------------------------------------------------
# AI Summary
# -------------------------------------------------------

st.subheader("🤖 AI Summary")

if average>=16:

    st.success(
        "Audience demonstrated excellent understanding of the presented topics."
    )

elif average>=12:

    st.warning(
        "Audience understood the concepts reasonably well, but some reinforcement is recommended."
    )

else:

    st.error(
        "Audience struggled significantly. Consider revisiting the topic before progressing."
    )

st.divider()

st.caption(
    "AudienceIQ Analytics Dashboard"
)