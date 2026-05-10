import tkinter as tk
from tkinter import ttk

from src.repository import add_expense


class AddExpenseWindow:

    def __init__(self, parent, refresh_callback):

        self.refresh_callback = refresh_callback

        self.window = tk.Toplevel(parent)

        self.window.title("Добавить расход")

        self.window.geometry("400x400")

        # ===== CATEGORY =====

        tk.Label(
            self.window,
            text="Категория"
        ).pack(pady=5)

        self.category_entry = tk.Entry(self.window)

        self.category_entry.pack()

        # ===== AMOUNT =====

        tk.Label(
            self.window,
            text="Сумма"
        ).pack(pady=5)

        self.amount_entry = tk.Entry(self.window)

        self.amount_entry.pack()

        # ===== TYPE =====

        tk.Label(
            self.window,
            text="Тип"
        ).pack(pady=5)

        self.type_combo = ttk.Combobox(
            self.window,
            values=["daily", "big", "rent"]
        )

        self.type_combo.pack()

        # ===== COMMENT =====

        tk.Label(
            self.window,
            text="Комментарий"
        ).pack(pady=5)

        self.comment_entry = tk.Entry(self.window)

        self.comment_entry.pack()

        # ===== BUTTON =====

        save_btn = ttk.Button(
            self.window,
            text="Сохранить",
            command=self.save_expense
        )

        save_btn.pack(pady=20)

    def save_expense(self):

        category = self.category_entry.get()

        amount = float(
            self.amount_entry.get()
        )

        type_ = self.type_combo.get()

        comment = self.comment_entry.get()

        add_expense(
            "2026-01-01",
            category,
            amount,
            type_,
            comment
        )

        self.refresh_callback()

        self.window.destroy()