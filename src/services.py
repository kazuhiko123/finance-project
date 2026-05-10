from .analysis import *

class FinanceService:

    def __init__(self, expenses, income):

        self.expenses = expenses
        self.income = income

    def get_stats(self):

        total_expenses = self.expenses["amount"].sum()

        total_income = self.income["amount"].sum()

        balance = total_income - total_expenses

        return {
            "expenses": round(total_expenses, 2),
            "income": round(total_income, 2),
            "balance": round(balance, 2)
        }

    def get_categories(self):

        return expenses_by_category(self.expenses)

    def get_monthly(self):

        return expenses_by_month(self.expenses)

    def get_weekday(self):

        return weekday_analysis(self.expenses)

    def get_last_expenses(self, limit=10):

        sorted_df = self.expenses.sort_values(
            by="date",
            ascending=False
        )

        return sorted_df.head(limit)

    def get_category_stats(self):

        return expenses_by_category(self.expenses)