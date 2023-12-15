import csv
from pathlib import Path

from user import add_user

filename = 'users.csv'
fieldnames = ['username', 'password']
path = Path(filename)

if not path.exists():
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        print(f'{filename} has been created successfully.')

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    try:
        success = add_user(writer)
        if success:
            print('User added successfully')
    except ValueError as e:
        print(f'Error: {e}')
