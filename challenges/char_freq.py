"""
    Write a function that takes a string as input and
    returns a dictionary with the count of each character in the string.
"""


def char_freq(sentence):
    char_dict = {}

    for char in sentence:
        if char == ' ':
            message = 'space'
        else:
            message = char

        if message in char_dict:
            char_dict[message] += 1
        else:
            char_dict[message] = 1

    return char_dict


user_in = input("Enter a sentence and I will count the frequency of each character: ")
result = char_freq(user_in)

# you use .items() to iterate through the key and the value simultaneously
for char, count in result.items():
    if count == 1:
        print(f'There is {count} {char} in {user_in}')
    elif count > 1:
        print(f'There are {count} {char}\'s in {user_in}')
