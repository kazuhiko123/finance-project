import pandas as pd

def expenses_by_category(df):
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)

def expenses_by_month(df):
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["amount"].sum()

def weekday_analysis(df):
    df["weekday"] =df["date"].dt.dayofweek
    return df.groupby("weekday")["amount"].sum()