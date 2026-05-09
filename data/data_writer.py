import pandas as pd
def append_expense(path, sheet_name, row: dict):
    df =pd.read_excel(path, sheet_name = sheet_name)

    df = pd.concat([df, pd.DataFrame([row])], ignore_index = True)

    with pd.ExcelWriter(path, engine = "openpyxl", mode ="a", if_sheet_exists = "replace") as writer:
        df.to_excel(writer, sheet_name = sheet_name, index = False)