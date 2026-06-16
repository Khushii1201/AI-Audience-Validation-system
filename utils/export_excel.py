import pandas as pd

from database.db import get_connection


def export_results():

    conn = get_connection()

    query = """
    SELECT *
    FROM responses
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    df.to_excel(
        "results.xlsx",
        index=False
    )

    conn.close()