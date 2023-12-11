# show_item.py
import pandas as pd


def show_all():
    df = pd.read_csv('inventory.csv')
    print(df.to_string(index=False))


def show_names():
    df = pd.read_csv('inventory.csv')
    names_column = df['Name']
    print(f'Item names available:\n{names_column.to_string(index=False)}')
