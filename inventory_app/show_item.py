import pandas as pd

df = pd.read_csv('inventory.csv', index_col=0)


def show_all():
    print(df)


def show_names():
    names_column = df['Name']
    print(names_column)
