from data_loader import load_all_data, load_expenses, load_income
from database import (
    init_db,
    save_expenses,
    save_income,
    load_expenses_db,
    load_income_db
)

from services import FinanceService


EXCEL_PATH = "data/Копия MyCosts_V2.xlsx"


# --- загрузка excel ---
sheets = load_all_data(EXCEL_PATH)

expenses = load_expenses(sheets)
income = load_income(sheets)


# --- база ---
init_db()

save_expenses(expenses)
save_income(income)


# --- загрузка из sqlite ---
expenses_db = load_expenses_db()
income_db = load_income_db()


# --- сервис ---
service = FinanceService(expenses_db, income_db)


print("СТАТИСТИКА")
print(service.get_stats())

print("ТОП КАТЕГОРИЙ")
print(service.get_categories().head())