import pandas as pd


def update_item(item_name):
    filename = 'inventory.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    choice = input("Would you like to update the price or the quantity?\n"
                   "> ").lower()
    if choice == 'price':
        new_price = float(input("What is the new price?\n"
                                "> "))
        df.loc[df['Name'] == item_name, 'Price'] = new_price
    elif choice == 'quantity':
        new_quantity = int(input("What is the new quantity?\n"
                                 "> "))
        df.loc[df['Name'] == item_name, 'Quantity'] = new_quantity
    else:
        print("Invalid choice. No updates were made.")

    # Write the modified DataFrame back to the CSV file
    df.to_csv(filename, index=False)
    print(f'Data has been updated successfully.')
