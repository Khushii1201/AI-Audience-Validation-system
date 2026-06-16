from database.db import get_connection


def get_total_responses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM responses"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result


def get_average_score():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(score) FROM responses"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result if result else 0
def get_leaderboard():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        user_name,
        SUM(score) as total_score
    FROM responses
    GROUP BY user_name
    ORDER BY total_score DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results
def get_session_stats(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        COUNT(*),
        AVG(score)
    FROM responses
    WHERE session_id=?
    """,(session_id,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_participant_scores():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        user_name,
        SUM(score)
    FROM responses
    GROUP BY user_name
    ORDER BY SUM(score) DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results