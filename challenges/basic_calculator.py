"""
    Create a basic calculator that takes two numbers and an operator
    (+, -, *, /) as input and performs the corresponding operation.

    UPDATE: adding a factorial equation
"""


def add():
    a = float(input('What\'s the first number to be added: '))
    b = float(input('And the second: '))
    print(f'Your answer is {int(a + b)}')


def sub():
    a = float(input('What\'s the number you want to subtract from: '))
    b = float(input('And the number to subtract: '))
    print(f'Your answer is {int(a - b)}')


def multiply():
    a = float(input('What\'s the number to be multiplied: '))
    b = float(input('And the number of times to multiply it: '))
    print(f'Your answer is {int(a * b)}')


def divide():
    a = float(input('What\'s the number to be divided by: '))
    b = float(input('And the number to go into it: '))
    print(f'Your answer is {int(a / b)}')


def factorial():
    num = int(input('What number do you want a factorial of: '))
    f = num
    fa = 1
    while f > 0:
        fa = fa * f
        f = f - 1
    print(f'The factorial of {num} is {fa}')


while True:
    print('Choose the number of the operation you would like to perform\n'
          '1. Addition\n'
          '2. Subtraction\n'
          '3. Multiplication\n'
          '4. Division\n'
          '5. Factorial \n'
          '6. Quit')
    user_input = int(input('> '))

    match user_input:
        case 1:
            add()

        case 2:
            sub()

        case 3:
            multiply()

        case 4:
            divide()

        case 5:
            factorial()

        case 6:
            print('Bye!')
            quit()
