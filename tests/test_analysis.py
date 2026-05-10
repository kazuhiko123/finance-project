import pandas as pd

from src.npanalysis import (
    average_expense,
    median_expense,
    max_expense,
    min_expense
)


def test_average_expense():

    data = pd.DataFrame({
        "amount": [100, 200, 300]
    })

    assert average_expense(data) == 200


def test_median_expense():

    data = pd.DataFrame({
        "amount": [100, 200, 300]
    })

    assert median_expense(data) == 200


def test_max_expense():

    data = pd.DataFrame({
        "amount": [100, 200, 300]
    })

    assert max_expense(data) == 300


def test_min_expense():

    data = pd.DataFrame({
        "amount": [100, 200, 300]
    })

    assert min_expense(data) == 100