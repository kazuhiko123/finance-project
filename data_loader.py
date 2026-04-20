import pandas as pd


def load_all_data(path: str):
    return pd.read_excel(path, sheet_name=None)


def load_expenses(sheets):
    # --- Повседневные ---
    daily = sheets["Повседневные"].copy()
    daily = daily.rename(columns={
        "Unnamed: 0": "date",
        "Категория": "category",
        "Стоимость": "amount"
    })
    daily["type"] = "daily"
    daily = daily[["date", "category", "amount", "type"]]

    # --- Крупные ---
    big = sheets["Крупные"].copy()
    big = big.rename(columns={
        "Дата": "date",
        "Категория": "category",
        "Стоимость": "amount"
    })
    big["type"] = "big"
    big = big[["date", "category", "amount", "type"]]

    # --- Квартира ---
    rent = sheets["Квартира"].copy()
    rent = rent.rename(columns={
        "Дата": "date",
        "Категория": "category",
        "Стоимость": "amount"
    })
    rent["type"] = "rent"
    rent = rent[["date", "category", "amount", "type"]]

    # --- объединение ---
    df = pd.concat([daily, big, rent], ignore_index=True)

    # очистка
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    return df


def load_income(sheets):
    income = sheets["Доходы"].copy()

    income = income.rename(columns={
        "Дата": "date",
        "Сумма": "amount",
        "Статья": "category"
    })

    income["type"] = "income"

    income = income[["date", "category", "amount", "type"]]

    income["date"] = pd.to_datetime(income["date"], errors="coerce")
    income = income.dropna(subset=["date", "amount"])

    return income