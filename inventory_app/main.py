# main.py
import csv
from pathlib import Path
from add_item import add_item
from remove_item import remove_item
from show_item import show_all, show_names
from update_item import update_item

filename = 'inventory.csv'
path = Path(filename)

if path.exists():
    while True:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            # If the file is empty, write the header
            if file.tell() == 0:
                writer.writerow(['Name', 'Price', 'Quantity'])

            choice = input('Choose an option: \n'
                           '1. Add new item\n'
                           '2. Remove item\n'
                           '3. Update inventory\n'
                           '4. Show all items\n'
                           '5. Exit application\n'
                           '> ')
            match choice:
                case '1':
                    add_item(writer)
                    file.flush()
                case '2':
                    show_names()
                    remove_item()
                    file.flush()
                case '3':
                    show_names()
                    item_to_update = input("Enter the name of the item to update: ")
                    update_item(item_to_update)
                    file.flush()
                case '4':
                    show_all()
                case '5':
                    print('Til next time!')
                    exit()
            print(f'Data has been added to {filename} successfully.')

else:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Quantity'])
        file.flush()
    print(f'{filename} has been created successfully.')
