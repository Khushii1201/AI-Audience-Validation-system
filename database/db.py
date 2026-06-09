import sqlite3

DB_NAME = "data/audience.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()