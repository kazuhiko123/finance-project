from .database import get_connection

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

def delete_expense(expense_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    conn.commit()

    conn.close()