import sqlite3
import os

# ----------------------------------------------------
# Database Path
# ----------------------------------------------------

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


# ----------------------------------------------------
# Connection
# ----------------------------------------------------

def get_connection():

    return sqlite3.connect(DB_NAME)


# ----------------------------------------------------
# Create Tables
# ----------------------------------------------------

def create_tables():

    os.makedirs(
        os.path.dirname(DB_NAME),
        exist_ok=True
    )

    conn = get_connection()

    cursor = conn.cursor()

    # ==================================================
    # Sessions
    # ==================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions(

            session_id INTEGER PRIMARY KEY AUTOINCREMENT,

            topic TEXT NOT NULL,

            difficulty TEXT DEFAULT 'Medium',

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    # ==================================================
    # Questions
    # ==================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions(

            question_id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            question TEXT,

            answer TEXT,

            FOREIGN KEY(session_id)
            REFERENCES sessions(session_id)

        )
        """
    )

    # ==================================================
    # Responses
    # ==================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS responses(

            response_id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER,

            question_id INTEGER,

            user_name TEXT,

            answer TEXT,

            score INTEGER,

            submitted_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES sessions(session_id),

            FOREIGN KEY(question_id)
            REFERENCES questions(question_id)

        )
        """
    )

    # ==================================================
    # Question Bank
    # ==================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS question_bank(

            bank_id INTEGER PRIMARY KEY AUTOINCREMENT,

            topic TEXT,

            difficulty TEXT,

            questions_json TEXT,

            usage_count INTEGER DEFAULT 0,

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()

    conn.close()