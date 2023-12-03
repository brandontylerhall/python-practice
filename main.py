# TODOne: familiarize on various string manipulation functions(methods?),
#  user input, defining variables, defining and using functions, etc
"""
    user_input = input('Tell me your name: ')

    print('cool facts about your name:\n')

    name_length = len(user_input)
    print(f'your name is {name_length} characters long')

    letter_5 = user_input[4]
    print(f'the 5th letter is: {letter_5}')

    letter = 'n'
    letter_freq = user_input.count(letter)
    # print('there are', letter_freq, letter, "'s in your name")
    print(f'there are {letter_freq} {letter}\'s in your name')

    reversed_name = ''.join(reversed(user_input))
    print(f'your name reversed is: {reversed_name}')


    def name_odd_even(input):
        if len(input) % 2 == 0:
            print('your name has an even amount of letters')
        else:
            print('your name has an odd amount of numbers in it')
            return
    name_odd_even(user_input)
"""
# TODOne: learn how to create dictionaries, what they do, and how to manipulate/use/whatever with them
"""
    data = {'Name': 'Zara', 'Age': 27, 'Class': 'First'}

    # Get all keys
    print(data.keys())

    # # Get all values
    print(data.values())
    #
    # # Print key1
    print(data['Name'])
    #
    # # Prints 7
    print(data['Age'])
    #
    # # Prints name and age
    print('Name', data['Name'])
    print('Age', data['Age'])
"""

# looping through a dictionary
"""
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }

    print(data)

    for key, value in data.items():
        print(key, value)

    # Looping their values directory (not in order)
    for value in data.values():
        print(value)
"""
# updating a dictionary
"""
    data = {'Name':'Zara','Age':7,'Class':'First'}

    data['Age'] = 8                    # update existing entry
    data['School'] = "DPS School"      # Add new entry

    print("data['Age']: ", data['Age'])
    print("data['School']: ", data['School'])
"""
