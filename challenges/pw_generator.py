import random

pw_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%',
            '&', '*', '+']


def pw_generator(inp):
    # LENGTH VARIABLE MUST BE CALLED "k" OR IT WILL NOT WORK
    # .choices takes the first argument and randomizes it, returning
    # a new list with the same elements, including duplicates
    password = random.choices(pw_chars, k=inp)  # choices allows user input for trimming of the list to that value
    return ''.join(password)


user_input = int(input('How many characters do you wish your password to be: '))
new_pw = pw_generator(user_input)
print(f'new pw = {new_pw}')
