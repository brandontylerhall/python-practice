import csv
from pathlib import Path
from run_app import run_app


def main():
    filename = 'inventory.csv'
    path = Path(filename)

    if path.exists():
        run_app()
    else:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Quantity'])
            file.close()
        print(f'{filename} has been created successfully.')
        run_app()


if __name__ == "__main__":
    main()
