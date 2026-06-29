from database.db import get_connection


# ----------------------------------------------------
# Total Responses
# ----------------------------------------------------

def get_total_responses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM responses"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ----------------------------------------------------
# Total Participants
# ----------------------------------------------------

def get_total_participants():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(DISTINCT user_name)
        FROM responses
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ----------------------------------------------------
# Average Score
# ----------------------------------------------------

def get_average_score():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(score)
        FROM responses
        """
    )

    avg = cursor.fetchone()[0]

    conn.close()

    return round(avg if avg else 0,2)


# ----------------------------------------------------
# Highest Score
# ----------------------------------------------------

def get_highest_score():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT MAX(total)

    FROM

    (

        SELECT

        SUM(score) as total

        FROM responses

        GROUP BY user_name

    )

    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result if result else 0


# ----------------------------------------------------
# Lowest Score
# ----------------------------------------------------

def get_lowest_score():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT MIN(total)

    FROM

    (

        SELECT

        SUM(score) as total

        FROM responses

        GROUP BY user_name

    )

    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result if result else 0


# ----------------------------------------------------
# Leaderboard
# ----------------------------------------------------

def get_leaderboard():

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


# ----------------------------------------------------
# Participant Scores
# ----------------------------------------------------

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


# ----------------------------------------------------
# Performance Distribution
# ----------------------------------------------------

def get_performance_distribution():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        user_name,

        SUM(score)

    FROM responses

    GROUP BY user_name

    """)

    scores = cursor.fetchall()

    conn.close()

    excellent = 0
    good = 0
    average = 0
    poor = 0

    for _, score in scores:

        if score >= 80:

            excellent += 1

        elif score >= 60:

            good += 1

        elif score >= 40:

            average += 1

        else:

            poor += 1

    return {

        "Excellent": excellent,

        "Good": good,

        "Average": average,

        "Needs Help": poor

    }


# ----------------------------------------------------
# Difficulty Analytics
# ----------------------------------------------------

def get_difficulty_statistics():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        s.difficulty,

        AVG(r.score)

    FROM responses r

    JOIN sessions s

    ON r.session_id=s.session_id

    GROUP BY s.difficulty

    """)

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# Topic Analytics
# ----------------------------------------------------

def get_topic_statistics():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        s.topic,

        AVG(r.score),

        COUNT(DISTINCT r.user_name)

    FROM responses r

    JOIN sessions s

    ON r.session_id=s.session_id

    GROUP BY s.topic

    ORDER BY AVG(r.score) DESC

    """)

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# Question Bank Usage
# ----------------------------------------------------

def get_question_bank_usage():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        topic,

        difficulty,

        usage_count

    FROM question_bank

    ORDER BY usage_count DESC

    LIMIT 5

    """)

    results = cursor.fetchall()

    conn.close()

    return results