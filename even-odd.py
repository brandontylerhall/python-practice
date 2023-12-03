"""
EVEN OR ODD
-----------
Write a program that takes an integer as input and prints whether it's even or odd
"""

user_input = input('Enter a number, any number, fool! ')


def even_odd(num):
    try:
        num = int(num)

        if num % 2 == 0:
            print(f'Your number is even, son!')
        elif num % 2 != 0:
            print(f'Your number ain\'t even, son!')
    except ValueError:
        print(f'I said a NUMBER, son!')


even_odd(user_input)
