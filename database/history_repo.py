from database.db import get_connection


# ----------------------------------------------------
# Session History
# ----------------------------------------------------

def get_all_sessions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        s.session_id,

        s.topic,

        s.difficulty,

        s.created_at,

        COUNT(DISTINCT r.user_name),

        IFNULL(AVG(r.score),0),

        IFNULL(MAX(r.score),0),

        COUNT(DISTINCT q.question_id)

    FROM sessions s

    LEFT JOIN responses r

    ON s.session_id = r.session_id

    LEFT JOIN questions q

    ON s.session_id = q.session_id

    GROUP BY s.session_id

    ORDER BY s.created_at DESC

    """)

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# One Session
# ----------------------------------------------------

def get_session_details(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        topic,

        difficulty,

        created_at

    FROM sessions

    WHERE session_id=?

    """,

    (session_id,)

    )

    result = cursor.fetchone()

    conn.close()

    return result


# ----------------------------------------------------
# Delete Session
# ----------------------------------------------------

def delete_session(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM responses WHERE session_id=?",

        (session_id,)

    )

    cursor.execute(

        "DELETE FROM questions WHERE session_id=?",

        (session_id,)

    )

    cursor.execute(

        "DELETE FROM sessions WHERE session_id=?",

        (session_id,)

    )

    conn.commit()

    conn.close()