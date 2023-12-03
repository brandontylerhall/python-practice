"""
    Create a basic calculator that takes two numbers and an operator
    (+, -, *, /) as input and performs the corresponding operation.
"""


def addition():
    a = float(input('What\'s the first number to be added: '))
    b = float(input('And the second: '))
    print(f'Your answer is {int(a + b)}')


# while True:
print('Choose the number of the operation you would like to perform\n'
      '1. Addition\n'
      '2. Subtraction\n'
      '3. Multiplication\n'
      '4. Division')
user_input = int(input('> '))

match user_input:
    case 1:
        addition()
