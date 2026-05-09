from db import get_connection


def add_expense(date, category, amount, type_, comment):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (
            date,
            category,
            amount,
            type,
            comment
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        date,
        category,
        amount,
        type_,
        comment
    ))

    conn.commit()

    conn.close()