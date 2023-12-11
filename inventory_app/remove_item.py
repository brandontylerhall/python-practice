import pandas as pd


def remove_item():
    item_to_remove = input("What would you like to remove?\n"
                           "> ")
    filename = 'inventory.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Drop the rows where the 'Name' column is equal to the specified item_name
    df = df.drop(df[df.Name == item_to_remove].index)

    # Write the modified DataFrame back to the CSV file
    df.to_csv(filename, index=False)

    print('Data has been removed successfully.')
