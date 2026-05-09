from data_loader import load_all_data, load_expenses, load_income
from db import get_connection, init_db

def migrate_from_excel(path):
    init_db()

    conn = get_connection()
    cursor = conn.cursor()
    sheets = load_all_data(path)
    expenses = load_expenses(sheets)
    income = load_income(sheets)

    # --- перенос расходов ---
    for _, row in expenses.iterrows():

        comment = None

        if "comment" in row:
            comment = row["comment"]

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
            str(row["date"]),
            row["category"],
            float(row["amount"]),
            row["type"],
            comment
        ))

    # --- перенос доходов ---
    for _, row in income.iterrows():

        cursor.execute("""
            INSERT INTO income (
                date,
                category,
                amount
            )
            VALUES (?, ?, ?)
        """, (
            str(row["date"]),
            row["category"],
            float(row["amount"])
        ))

    conn.commit()
    conn.close()

    print("Трансфер завершен")