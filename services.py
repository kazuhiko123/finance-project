from analysis import *

class FinanceService:
    def __init__(self, expenses, income):
        self.expenses = expenses
        self.income = income

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