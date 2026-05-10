import tkinter as tk
from tkinter import ttk

from src.ui.add_expense_window import AddExpenseWindow
from src.ui.monthly_chart import MonthlyChart

from src.database import *

from src.services import *


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Finance App")

        self.root.geometry("1000x700")

        # ===== DATA =====

        expenses = load_expenses_db()

        income = load_income_db()

        self.service = FinanceService(
            expenses,
            income
        )

        # ===== HEADER =====

        title = tk.Label(
            self.root,
            text="Finance Dashboard",
            font=("Arial", 24)
        )

        title.pack(pady=20)

        # ===== STATS =====

        self.stats_frame = tk.Frame(self.root)

        self.stats_frame.pack(pady=10)

        self.balance_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 16)
        )

        self.balance_label.pack()

        self.income_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 14)
        )

        self.income_label.pack()

        self.expenses_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 14)
        )

        self.expenses_label.pack()

        # ===== BUTTON =====

        add_expense_btn = ttk.Button(
            self.root,
            text="Добавить расход",
            command=self.open_add_expense
        )

        add_expense_btn.pack(pady=20)

        # ===== TABLE =====

        table_title = tk.Label(
            self.root,
            text="Последние расходы",
            font=("Arial", 16)
        )

        table_title.pack(pady=10)

        columns = (
            "date",
            "category",
            "amount",
            "type"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(col, width=150)

        self.tree.pack(fill="both", expand=True, padx=20)

        # ===== INIT =====

        self.refresh_dashboard()

    def refresh_dashboard(self):

        expenses = load_expenses_db()

        income = load_income_db()

        self.service = FinanceService(
            expenses,
            income
        )

        stats = self.service.get_stats()

        self.balance_label.config(
            text=f"Баланс: {stats['balance']}"
        )

        self.income_label.config(
            text=f"Доходы: {stats['income']}"
        )

        self.expenses_label.config(
            text=f"Расходы: {stats['expenses']}"
        )

        # ===== CLEAR TABLE =====

        for item in self.tree.get_children():

            self.tree.delete(item)

        # ===== INSERT DATA =====

        last_expenses = self.service.get_last_expenses()

        for _, row in last_expenses.iterrows():

            self.tree.insert(
                "",
                "end",
                values=(
                    row["date"],
                    row["category"],
                    row["amount"],
                    row["type"]
                )
            )

    def open_add_expense(self):

        AddExpenseWindow(
            self.root,
            self.refresh_dashboard
        )

    def run(self):

        self.root.mainloop()