"""
Write a program that converts temperatures between Celsius and Fahrenheit.
Prompt the user to enter a temperature in one scale and print the converted temperature.
"""


def f_to_c():
    try:
        f = float(input('What is the temperature you want to convert in °F: '))
        c = round((5 / 9) * (f - 32), 2)
        print(f'Your Queen Unit temperature is: {c}°C')
    except ValueError:
        print('That isn\'t Freedom OR a Queen Unit, brah. Try again.')


def c_to_f():
    try:
        f = float(input('What is the temperature you want to convert in °C: '))
        c = round((9 / 5) * f + 32, 2)
        print(f'Your Freedom Unit temperature is: {c}°F')
    except ValueError:
        print('That isn\'t Freedom OR a Queen Unit, brah. Try again.')


while True:
    print('Do you want to convert: \n'
          '1. Freedom Units to Queen Units \n'
          '2. Queen Units to Freedom Units \n'
          '3. Quit like the yella-bellied coward you are')
    user_input = int(input('> '))
    match user_input:
        case 1:
            f_to_c()
        case 2:
            c_to_f()
        case 3:
            print('Good riddance, coward...')
            quit()
