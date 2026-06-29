import json

from database.db import get_connection


# ----------------------------------------------------
# Save Question Set
# ----------------------------------------------------

def save_question_bank(
    topic,
    difficulty,
    questions
):

    conn = get_connection()
    cursor = conn.cursor()

    topic = topic.strip().lower()

    questions_json = json.dumps(
        questions
    )

    # Check if question set already exists
    cursor.execute(
        """
        SELECT bank_id
        FROM question_bank
        WHERE topic = ?
        AND difficulty = ?
        """,
        (
            topic,
            difficulty
        )
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE question_bank

            SET
                questions_json = ?

            WHERE
                bank_id = ?
            """,
            (
                questions_json,
                existing[0]
            )
        )

    else:

        cursor.execute(
            """
            INSERT INTO question_bank(

                topic,

                difficulty,

                questions_json

            )

            VALUES(?,?,?)

            """,
            (
                topic,
                difficulty,
                questions_json
            )
        )

    conn.commit()
    conn.close()


# ----------------------------------------------------
# Search Question Sets
# ----------------------------------------------------

def search_question_bank(
    topic,
    difficulty
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            bank_id,

            topic,

            difficulty,

            questions_json,

            usage_count,

            created_at

        FROM question_bank

        WHERE

            LOWER(topic) LIKE ?

        AND

            difficulty = ?

        ORDER BY

            usage_count DESC,

            created_at DESC

        """,
        (
            f"%{topic.lower()}%",
            difficulty
        )
    )

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# Load Question Set
# ----------------------------------------------------

def get_question_bank(
    bank_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            questions_json

        FROM question_bank

        WHERE bank_id = ?
        """,
        (bank_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:

        return json.loads(
            result[0]
        )

    return []


# ----------------------------------------------------
# Increase Usage
# ----------------------------------------------------

def increase_usage(
    bank_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE question_bank

        SET usage_count = usage_count + 1

        WHERE bank_id = ?
        """,
        (bank_id,)
    )

    conn.commit()
    conn.close()


# ----------------------------------------------------
# All Question Sets
# ----------------------------------------------------

def get_all_question_banks():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            bank_id,

            topic,

            difficulty,

            questions_json,

            usage_count,

            created_at

        FROM question_bank

        ORDER BY

            created_at DESC
        """
    )

    results = cursor.fetchall()

    conn.close()

    return results


# ----------------------------------------------------
# Delete Question Set
# ----------------------------------------------------

def delete_question_bank(
    bank_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM question_bank

        WHERE bank_id = ?
        """,
        (bank_id,)
    )

    conn.commit()
    conn.close()


# ----------------------------------------------------
# Count Question Sets
# ----------------------------------------------------

def get_question_bank_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM question_bank
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


# ----------------------------------------------------
# Topic Exists?
# ----------------------------------------------------

def question_bank_exists(
    topic,
    difficulty
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT bank_id

        FROM question_bank

        WHERE topic=?

        AND difficulty=?
        """,
        (
            topic.lower(),
            difficulty
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None