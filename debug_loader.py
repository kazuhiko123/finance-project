import pandas as pd


def inspect_excel(path):
    sheets = pd.read_excel(path, sheet_name=None)

    for name, df in sheets.items():
        print(f"\n=== ЛИСТ: {name} ===")
        print("Колонки:", list(df.columns))
        print("Размер:", df.shape)
        print(df.head(3))


if __name__ == "__main__":
    inspect_excel("/finance-project/data/Копия MyCosts_V2.xlsx")