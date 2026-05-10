import tkinter as tk
from tkinter import ttk

from ..repository import delete_expense
from .add_expense_window import AddExpenseWindow
from .monthly_chart import MonthlyChart
from .category_chart import CategoryChart

from ..database import *
from ..services import *
from ..npanalysis import analytics_report

class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Finance Dashboard")

        self.root.geometry("1200x800")

        self.notebook = ttk.Notebook(self.root)

        self.notebook.pack(
            fill="both",
            expand=True
        )

        # TABS

        self.dashboard_tab = tk.Frame(self.notebook)

        self.analytics_tab = tk.Frame(self.notebook)

        self.expenses_tab = tk.Frame(self.notebook)

        # ADD TABS

        self.notebook.add(
            self.dashboard_tab,
            text="Dashboard"
        )

        self.notebook.add(
            self.analytics_tab,
            text="Analytics"
        )

        self.notebook.add(
            self.expenses_tab,
            text="Expenses"
        )

        # DATA

        expenses = load_expenses_db()

        income = load_income_db()

        self.service = FinanceService(
            expenses,
            income
        )

        # HEADER

        header_frame = tk.Frame(self.dashboard_tab)

        header_frame.pack(fill="x", pady=10)

        title = tk.Label(
            header_frame,
            text="Finance Dashboard",
            font=("Arial", 28)
        )

        title.pack()

        # STATS

        self.stats_frame = tk.Frame(self.dashboard_tab)

        self.stats_frame.pack(fill="x", pady=10)

        self.balance_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 18)
        )

        self.balance_label.pack()

        self.income_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 16)
        )

        self.income_label.pack()

        self.expenses_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Arial", 16)
        )

        self.expenses_label.pack()

        stats = analytics_report(expenses)

        stats_text = (
            f"Средняя трата: {stats['average']:.2f}\n"
            f"Медиана: {stats['median']:.2f}\n"
            f"Макс трата: {stats['max']:.2f}"
        )

        stats_label = tk.Label(
            self.dashboard_tab,
            text=stats_text,
            font=("Arial", 12),
            justify="left"
        )

        stats_label.pack(pady=10)

        # CHARTS


        charts_frame = tk.Frame(self.analytics_tab)

        charts_frame.pack(fill="x", padx=20, pady=20)

        # MONTHLY CHART

        monthly_data = self.service.get_monthly()

        monthly_chart_frame = tk.Frame(charts_frame)

        monthly_chart_frame.pack(side="left", expand=True)

        self.chart = MonthlyChart(
            monthly_chart_frame,
            monthly_data
        )

        # CATEGORY CHART

        category_data = self.service.get_category_stats()

        category_chart_frame = tk.Frame(charts_frame)

        category_chart_frame.pack(side="right", expand=True)

        self.category_chart = CategoryChart(
            category_chart_frame,
            category_data
        )

        # BUTTONS

        buttons_frame = tk.Frame(self.expenses_tab)

        buttons_frame.pack(fill="x", pady=10)

        add_expense_btn = ttk.Button(
            buttons_frame,
            text="Добавить расход",
            command=self.open_add_expense
        )

        add_expense_btn.pack(side="left", padx=20)

        delete_btn = ttk.Button(
            buttons_frame,
            text="Удалить расход",
            command=self.delete_selected_expense
        )

        delete_btn.pack(side="left")

        # TABLE

        table_frame = tk.Frame(self.expenses_tab)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        table_title = tk.Label(
            table_frame,
            text="Последние расходы",
            font=("Arial", 18)
        )

        table_title.pack(pady=10)

        columns = (
            "id",
            "date",
            "category",
            "amount",
            "type"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(
                col,
                width=150,
                anchor="center"
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

        # INIT

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
            text=f"Баланс: {stats['balance']:.2f}"
        )

        self.income_label.config(
            text=f"Доходы: {stats['income']:.2f}"
        )

        self.expenses_label.config(
            text=f"Расходы: {stats['expenses']:.2f}"
        )

        # CLEAR TABLE

        for item in self.tree.get_children():

            self.tree.delete(item)

        # INSERT DATA

        last_expenses = self.service.get_last_expenses()

        for _, row in last_expenses.iterrows():

            self.tree.insert(
                "",
                "end",
                values=(
                    row["id"],
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

    def delete_selected_expense(self):

        selected_item = self.tree.selection()

        if not selected_item:
            return

        item = self.tree.item(selected_item)

        values = item["values"]

        expense_id = values[0]

        delete_expense(expense_id)

        self.refresh_dashboard()

    def run(self):

        self.root.mainloop()