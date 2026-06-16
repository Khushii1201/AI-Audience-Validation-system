from database.db import get_connection


def save_question(
        session_id,
        question,
        answer
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO questions(
            session_id,
            question,
            answer
        )
        VALUES(?,?,?)
        """,
        (
            session_id,
            question,
            answer
        )
    )

    conn.commit()
    conn.close()


def get_correct_answer(question_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT answer
        FROM questions
        WHERE question_id = ?
        """,
        (question_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return ""


def get_questions_by_session(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            question_id,
            question,
            answer
        FROM questions
        WHERE session_id = ?
        """,
        (session_id,)
    )

    questions = cursor.fetchall()

    conn.close()

    return questions