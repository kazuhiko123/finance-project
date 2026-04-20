import sys
import os

sys.path.append(os.path.dirname(__file__))
from data_loader import load_all_data, load_expenses, load_income

sheets = load_all_data("data/Копия MyCosts_V2.xlsx")

expenses = load_expenses(sheets)
income = load_income(sheets)

print("РАСХОДЫ:")
print(len(expenses))
print(expenses["type"].value_counts())

print("ДОХОДЫ:")
print(len(income))