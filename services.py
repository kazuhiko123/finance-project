from data_loader import load_all_data, load_expenses, load_income
from analysis import *

class FinanceService:
    def __init__(self, path):
        self.path = path
        self.reload_data()

    def reload_data(self):
        sheets =load_all_data(self.path)
        self.expenses = load_expenses(sheets)
        self.income = load_income(sheets)

    def get_stats(self):
        return {
            "expenses": self.expenses["amount"].sum(),
            "income": self.income["amount"].sum(),
            "balance": self.income["amount"].sum() - self.expenses["amount"].sum(),
        }

    def get_categories(self):
        return expenses_by_category(self.expenses)

    def get_monthly(self):
        return expenses_by_month(self.expenses)

    def get_weekday(self):
        return weekday_analysis(self.expenses)