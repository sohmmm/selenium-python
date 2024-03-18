import pandas as pd


def read_excel(filepath, sheet_name):
    df = None
    try:
        df = pd.read_excel(filepath, sheet_name)
    except Exception as e:
        print(e)

    return df
