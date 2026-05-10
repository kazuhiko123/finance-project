def expense_generator(expenses):

    for _, row in expenses.iterrows():

        yield (
            row["date"],
            row["category"],
            row["amount"]
        )


def large_expenses_generator(
    expenses,
    threshold=10000
):

    for _, row in expenses.iterrows():

        if row["amount"] >= threshold:

            yield row