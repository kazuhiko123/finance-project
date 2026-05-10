import numpy as np


def average_expense(expenses):

    return np.mean(expenses["amount"])


def median_expense(expenses):

    return np.median(expenses["amount"])


def max_expense(expenses):

    return np.max(expenses["amount"])


def min_expense(expenses):

    return np.min(expenses["amount"])


def expense_std(expenses):

    return np.std(expenses["amount"])


def analytics_report(expenses):

    report = {
        "average": average_expense(expenses),
        "median": median_expense(expenses),
        "max": max_expense(expenses),
        "min": min_expense(expenses),
        "std": expense_std(expenses),
    }

    return report