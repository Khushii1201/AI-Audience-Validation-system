from database.db import get_connection


def get_all_sessions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        session_id,
        topic
    FROM sessions
    ORDER BY session_id DESC
    """)

    sessions = cursor.fetchall()

    conn.close()

    return sessions