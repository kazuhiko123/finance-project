import pandas as pd
from db import get_connection

conn = get_connection()

expenses = pd.read_sql("SELECT * FROM expenses", conn)
income = pd.read_sql("SELECT * FROM income", conn)

print("РАСХОДЫ:")
print(expenses.head())
print(len(expenses))

print()

print("ДОХОДЫ:")
print(income.head())
print(len(income))

conn.close()