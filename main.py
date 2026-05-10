import argparse

from src.database import (
    load_expenses_db,
    load_income_db
)

from src.services import FinanceService
from src.npanalysis import analytics_report

from src.ui.main_window import MainWindow


def show_stats():

    expenses = load_expenses_db()

    stats = analytics_report(expenses)

    print("\n=== FINANCE STATS ===")

    print(
        f"Average expense: "
        f"{stats['average']:.2f}"
    )

    print(
        f"Median expense: "
        f"{stats['median']:.2f}"
    )

    print(
        f"Max expense: "
        f"{stats['max']:.2f}"
    )

    print(
        f"Min expense: "
        f"{stats['min']:.2f}"
    )


def show_analytics():

    expenses = load_expenses_db()

    income = load_income_db()

    service = FinanceService(
        expenses,
        income
    )

    monthly = service.get_monthly()

    categories = service.get_category_stats()

    print("\n=== MONTHLY EXPENSES ===")

    print(monthly)

    print("\n=== CATEGORY STATS ===")

    print(categories)


def run_gui():

    app = MainWindow()

    app.run()


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "mode",
        nargs="?",
        default="gui"
    )

    args = parser.parse_args()

    if args.mode == "stats":

        show_stats()

    elif args.mode == "analytics":

        show_analytics()

    else:

        run_gui()


if __name__ == "__main__":

    main()