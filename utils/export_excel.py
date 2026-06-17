from openpyxl import Workbook

from database.db import get_connection


def export_results():

    wb = Workbook()

    ws = wb.active

    ws.title = "Results"

    ws.append(
        [
            "Participant",
            "Total Score"
        ]
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        user_name,
        SUM(score)
    FROM responses
    GROUP BY user_name
    ORDER BY SUM(score) DESC
    """)

    results = cursor.fetchall()

    conn.close()

    for row in results:

        ws.append(row)

    filename = "results.xlsx"

    wb.save(
        filename
    )

    return filename