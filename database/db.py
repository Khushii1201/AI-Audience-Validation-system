import sqlite3
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DB_NAME = os.path.join(
    BASE_DIR,
    "data",
    "audience.db"
)
print(DB_NAME)


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    os.makedirs(
        os.path.dirname(DB_NAME),
        exist_ok=True
    )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        question TEXT,
        answer TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS responses(
        response_id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER,
        question_id INTEGER,
        user_name TEXT,
        answer TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()