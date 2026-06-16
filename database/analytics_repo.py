from database.db import get_connection

def get_total_responses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM responses"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count