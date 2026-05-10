from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class MonthlyChart:

    def __init__(self, parent, monthly_data):

        self.figure = Figure(
            figsize=(6, 4),
            dpi=100
        )

        self.ax = self.figure.add_subplot(111)

        months = monthly_data.index.astype(str)

        amounts = monthly_data.values

        self.ax.plot(
            months,
            amounts,
            marker="o"
        )

        self.ax.set_title(
            "Расходы по месяцам"
        )

        self.ax.set_xlabel(
            "Месяц"
        )

        self.ax.set_ylabel(
            "Сумма"
        )

        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=parent
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            pady=20
        )