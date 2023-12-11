def add_item(writer):
    item_name = input('Enter the item\'s name: ')
    price = int(input('Enter the item\'s price: '))
    quantity = int(input('Enter the item\'s quantity: '))
    user_data = [item_name, price, quantity]

    writer.writerow(user_data)
