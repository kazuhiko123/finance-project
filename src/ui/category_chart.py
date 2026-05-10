from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt


class CategoryChart:

    def __init__(self, parent, data):

        # SORT

        data = data.sort_values(
            ascending=False
        )

        # TOP CATEGORIES

        top = data.head(7)

        other = data.iloc[7:].sum()

        if other > 0:

            top["Другое"] = other

        # FIGURE

        fig, ax = plt.subplots(
            figsize=(5, 5)
        )

        ax.pie(
            top.values,
            labels=top.index,
            autopct="%1.1f%%"
        )

        ax.set_title(
            "Расходы по категориям"
        )

        self.canvas = FigureCanvasTkAgg(
            fig,
            master=parent
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack()