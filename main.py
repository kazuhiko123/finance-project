import argparse

from src.database import (
    load_expenses_db,
    load_income_db
)

from src.services import FinanceService
from src.npanalysis import analytics_report

from src.ui.main_window import MainWindow

from src.generators import (
    expense_generator,
    large_expenses_generator
)

from src.decorators import (
    log_function_call,
    measure_time
)

@log_function_call
@measure_time
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


@log_function_call
@measure_time
def show_analytics():

    expenses = load_expenses_db()

    income = load_income_db()

    service = FinanceService(
        expenses,
        income
    )

    monthly = service.get_monthly()

    categories = service.get_category_stats()

    print("\nMONTHLY EXPENSES")

    print(monthly)

    print("\nCATEGORY STATS")

    print(categories)

    print("\nGENERATED EXPENSES")

    generator = expense_generator(expenses)

    for expense in generator:

        print(expense)

        break

    print("\n=== LARGE EXPENSES ===")

    large_generator = large_expenses_generator(
        expenses
    )

    for expense in large_generator:

        print(
            expense["category"],
            expense["amount"]
        )


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