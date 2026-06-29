from database.db import get_connection


# -------------------------------------------------------
# Save Response
# -------------------------------------------------------

def save_response(
    session_id,
    question_id,
    user_name,
    answer,
    score
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO responses(

            session_id,

            question_id,

            user_name,

            answer,

            score

        )

        VALUES(?,?,?,?,?)

        """,

        (

            session_id,

            question_id,

            user_name,

            answer,

            score

        )

    )

    conn.commit()

    conn.close()


# -------------------------------------------------------
# Get Responses By Session
# -------------------------------------------------------

def get_responses_by_session(
    session_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        user_name,

        question_id,

        answer,

        score

    FROM responses

    WHERE session_id=?

    ORDER BY user_name

    """,

    (session_id,)

    )

    results = cursor.fetchall()

    conn.close()

    return results


# -------------------------------------------------------
# Get Responses By User
# -------------------------------------------------------

def get_user_responses(
    user_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        session_id,

        question_id,

        answer,

        score

    FROM responses

    WHERE user_name=?

    """,

    (user_name,)

    )

    results = cursor.fetchall()

    conn.close()

    return results


# -------------------------------------------------------
# Delete Responses
# -------------------------------------------------------

def delete_session_responses(
    session_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        """

        DELETE FROM responses

        WHERE session_id=?

        """,

        (session_id,)

    )

    conn.commit()

    conn.close()


# -------------------------------------------------------
# Total Score
# -------------------------------------------------------

def get_total_score(
    user_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        SUM(score)

    FROM responses

    WHERE user_name=?

    """,

    (user_name,)

    )

    result = cursor.fetchone()[0]

    conn.close()

    return result if result else 0


# -------------------------------------------------------
# Average Score
# -------------------------------------------------------

def get_average_score_by_user(
    user_name
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        AVG(score)

    FROM responses

    WHERE user_name=?

    """,

    (user_name,)

    )

    result = cursor.fetchone()[0]

    conn.close()

    return round(result if result else 0,2)