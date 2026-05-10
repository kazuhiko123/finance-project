import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MonthlyChart(tk.Frame):

    def __init__(self, parent, monthly_data):

        super().__init__(parent)

        # ВАЖНО
        self.pack(fill="both", expand=True)

        # Подписи месяцев
        labels = [
            str(period)
            for period in monthly_data.index
        ]

        # Создание графика
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.plot(labels, monthly_data.values)

        ax.set_title("Расходы по месяцам")

        ax.set_xlabel("Месяц")

        ax.set_ylabel("Сумма")

        # Поворот подписей
        plt.xticks(rotation=45)

        # Красивые отступы
        fig.tight_layout()

        # Canvas
        canvas = FigureCanvasTkAgg(
            fig,
            master=self
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )