from database.db import get_connection

def save_response(
        session_id,
        question_id,
        user_name,
        answer,
        score
):

    print(
        "Saving:",
        session_id,
        question_id,
        user_name,
        answer,
        score
    )

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

    print("Inserted row")

    conn.close()