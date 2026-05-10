import sqlite3
import pandas as pd


DB_NAME = "finance.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        type TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()


def save_expenses(df: pd.DataFrame):
    conn = get_connection()

    df.to_sql(
        "expenses",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def save_income(df: pd.DataFrame):
    conn = get_connection()

    df.to_sql(
        "income",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def load_expenses_db():
    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM expenses",
        conn
    )

    conn.close()

    return df


def load_income_db():
    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM income",
        conn
    )

    conn.close()

    return df