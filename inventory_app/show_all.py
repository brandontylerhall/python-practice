import pandas as pd


def show_all():
    df = pd.read_csv('inventory.csv', index_col=0)
    print(df)
