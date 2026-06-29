from database.db import get_connection


# ----------------------------------------------------
# Save Question
# ----------------------------------------------------

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


# ----------------------------------------------------
# Get Correct Answer
# ----------------------------------------------------

def get_correct_answer(
    question_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT answer

        FROM questions

        WHERE question_id=?

        """,
        (question_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:

        return result[0]

    return ""


# ----------------------------------------------------
# Get Questions By Session
# ----------------------------------------------------

def get_questions_by_session(
    session_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            question_id,

            question,

            answer

        FROM questions

        WHERE session_id=?

        ORDER BY question_id

        """,
        (session_id,)
    )

    questions = cursor.fetchall()

    conn.close()

    return questions


# ----------------------------------------------------
# Update Question
# ----------------------------------------------------

def update_question(
    question_id,
    question,
    answer
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE questions

        SET

            question=?,

            answer=?

        WHERE question_id=?

        """,
        (
            question,
            answer,
            question_id
        )
    )

    conn.commit()

    conn.close()


# ----------------------------------------------------
# Delete Question
# ----------------------------------------------------

def delete_question(
    question_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM questions

        WHERE question_id=?

        """,
        (question_id,)
    )

    conn.commit()

    conn.close()


# ----------------------------------------------------
# Delete All Questions Of Session
# ----------------------------------------------------

def delete_questions_by_session(
    session_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM questions

        WHERE session_id=?

        """,
        (session_id,)
    )

    conn.commit()

    conn.close()


# ----------------------------------------------------
# Count Questions
# ----------------------------------------------------

def get_question_count(
    session_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM questions

        WHERE session_id=?

        """,
        (session_id,)
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


# ----------------------------------------------------
# Search Questions
# ----------------------------------------------------

def search_questions(
    keyword
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            question_id,

            question,

            answer

        FROM questions

        WHERE LOWER(question)

        LIKE ?

        """,
        (
            f"%{keyword.lower()}%",
        )
    )

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# Get All Questions
# ----------------------------------------------------

def get_all_questions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            question_id,

            session_id,

            question,

            answer

        FROM questions

        ORDER BY question_id DESC

        """
    )

    questions = cursor.fetchall()

    conn.close()

    return questions