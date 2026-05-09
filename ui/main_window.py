import tkinter as tk
from tkinter import ttk

from ui.add_expense_window import AddExpenseWindow


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Finance App")

        self.root.geometry("900x600")

        # ===== HEADER =====

        title = tk.Label(
            self.root,
            text="Finance Dashboard",
            font=("Arial", 20)
        )

        title.pack(pady=20)

        # ===== BUTTONS =====

        add_expense_btn = ttk.Button(
            self.root,
            text="Добавить расход",
            command=self.open_add_expense
        )

        add_expense_btn.pack(pady=10)

        # ===== STATS =====

        self.stats_label = tk.Label(
            self.root,
            text="Статистика появится здесь",
            font=("Arial", 12)
        )

        self.stats_label.pack(pady=20)

    def open_add_expense(self):

        AddExpenseWindow(self.root)

    def run(self):

        self.root.mainloop()