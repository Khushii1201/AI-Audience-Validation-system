from database.db import get_connection

def create_session(topic):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sessions(topic) VALUES(?)",
        (topic,)
    )

    conn.commit()

    session_id = cursor.lastrowid

    conn.close()

    return session_id