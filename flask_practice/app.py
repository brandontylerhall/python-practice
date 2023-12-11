import csv
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)


def write_to_csv(data):
    filename = 'inventory.csv'
    fieldnames = ['Name', 'Price', 'Quantity']
    path = Path(filename)

    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not path.exists():
            writer.writeheader()
        writer.writerow(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def handle_form():
    name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    form_data = {'Name': name, 'Price': price, 'Quantity': quantity}

    write_to_csv(form_data)

    return 'Data written successfully'


if __name__ == '__main__':
    app.run()
