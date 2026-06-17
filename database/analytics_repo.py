from database.db import get_connection


def get_total_responses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM responses
    """)

    result = cursor.fetchone()

    conn.close()

    return result[0]


def get_average_score():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(score)
    FROM responses
    """)

    result = cursor.fetchone()

    conn.close()

    if result[0] is None:

        return 0

    return float(result[0])


def get_highest_score():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT MAX(total_score)
    FROM
    (
        SELECT
            user_name,
            SUM(score) as total_score
        FROM responses
        GROUP BY user_name
    )
    """)

    result = cursor.fetchone()

    conn.close()

    if result[0] is None:

        return 0

    return result[0]


def get_participant_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(DISTINCT user_name)
    FROM responses
    """)

    result = cursor.fetchone()

    conn.close()

    return result[0]


def get_participant_scores():

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


def get_leaderboard():

    return get_participant_scores()


def get_performance_distribution():

    participants = get_participant_scores()

    excellent = 0
    good = 0
    needs_help = 0

    for _, score in participants:

        if score >= 80:

            excellent += 1

        elif score >= 60:

            good += 1

        else:

            needs_help += 1

    return (
        excellent,
        good,
        needs_help
    )


def get_session_summary():

    return {
        "responses":
            get_total_responses(),

        "participants":
            get_participant_count(),

        "average_score":
            get_average_score(),

        "highest_score":
            get_highest_score()
    }