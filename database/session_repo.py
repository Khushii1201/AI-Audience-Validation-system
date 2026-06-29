from database.db import get_connection


# ----------------------------------------------------
# Create Session
# ----------------------------------------------------

def create_session(
    topic,
    difficulty="Medium"
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sessions(

            topic,

            difficulty

        )

        VALUES(?,?)

        """,
        (
            topic.strip(),
            difficulty
        )
    )

    conn.commit()

    session_id = cursor.lastrowid

    conn.close()

    return session_id


# ----------------------------------------------------
# Get Session
# ----------------------------------------------------

def get_session(
    session_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            session_id,

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
# Get All Sessions
# ----------------------------------------------------

def get_all_sessions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            session_id,

            topic,

            difficulty,

            created_at

        FROM sessions

        ORDER BY created_at DESC

        """
    )

    sessions = cursor.fetchall()

    conn.close()

    return sessions


# ----------------------------------------------------
# Search Sessions
# ----------------------------------------------------

def search_sessions(
    keyword
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            session_id,

            topic,

            difficulty,

            created_at

        FROM sessions

        WHERE LOWER(topic)

        LIKE ?

        ORDER BY created_at DESC

        """,
        (
            f"%{keyword.lower()}%",
        )
    )

    sessions = cursor.fetchall()

    conn.close()

    return sessions


# ----------------------------------------------------
# Delete Session
# ----------------------------------------------------

def delete_session(
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

    cursor.execute(
        """
        DELETE FROM questions

        WHERE session_id=?

        """,
        (session_id,)
    )

    cursor.execute(
        """
        DELETE FROM sessions

        WHERE session_id=?

        """,
        (session_id,)
    )

    conn.commit()

    conn.close()


# ----------------------------------------------------
# Total Sessions
# ----------------------------------------------------

def get_total_sessions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM sessions
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ----------------------------------------------------
# Latest Session
# ----------------------------------------------------

def get_latest_session():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            session_id,

            topic,

            difficulty,

            created_at

        FROM sessions

        ORDER BY session_id DESC

        LIMIT 1
        """
    )

    result = cursor.fetchone()

    conn.close()

    return result