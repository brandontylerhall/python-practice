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


f_to_c()
c_to_f()
