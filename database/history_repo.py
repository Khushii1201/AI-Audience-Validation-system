from database.db import get_connection


def get_all_sessions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        s.session_id,
        s.topic,
        COUNT(DISTINCT r.user_name),
        AVG(r.score)
    FROM sessions s
    LEFT JOIN responses r
    ON s.session_id = r.session_id
    GROUP BY s.session_id
    ORDER BY s.session_id DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results