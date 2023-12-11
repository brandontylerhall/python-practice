# show_item.py
import pandas as pd

try:
    df = pd.read_csv('inventory.csv')


    def show_all():
        print(df.to_string(index=False))


    def show_names():
        names_column = df['Name']
        print(f'Item names available:\n{names_column.to_string(index=False)}')

except FileNotFoundError:
    print("Error: 'inventory.csv' file not found.")
