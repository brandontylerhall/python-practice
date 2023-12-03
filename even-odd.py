"""
EVEN OR ODD
-----------
Write a program that takes an integer as input and prints whether it's even or odd
"""


def even_odd(num):
    try:
        num = int(num)

        if num % 2 == 0:
            print(f'Your number is even, son!')
        elif num % 2 != 0:
            print(f'Your number ain\'t even, son!')
    except ValueError:
        print(f'I said a NUMBER, son!')


while True:
    user_input = input('Enter a number, any number. Hurry up, sucka! ')
    even_odd(user_input)

    another_input = input('You wanna try again fool‽ (yes/no) ').lower()

    if another_input in ['yes', 'y']:
        user_input = input("What's that number then, son‽ ")
        even_odd(user_input)
    elif another_input in ['no', 'n']:
        print('See ya later then, sucka!')
        break
    else:
        print('Wrong answer, sucka! I said (yes/no)! ')
