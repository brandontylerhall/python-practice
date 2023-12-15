def f_to_c():
    try:
        f = float(input('\nWhat is the temperature you want to convert in °F:\n> '))
        c = round((5 / 9) * (f - 32), 2)
        print(f'\nYour Queen Unit temperature is: {c}°C. Wowee!\n')
    except ValueError:
        print('That isn\'t Freedom OR a Queen Unit, brah. Try again.')


def c_to_f():
    try:
        f = float(input('\nWhat is the temperature you want to convert in °C:\n> '))
        c = round((9 / 5) * f + 32, 2)
        print(f'\nYour Freedom Unit temperature is: {c}°F. Wowee!\n')
    except ValueError:
        print('That isn\'t Freedom OR a Queen Unit, brah. Try again.')


def temp_convert():
    while True:
        print('What do you want to convert: \n'
              '1. Freedom Units to Queen Units \n'
              '2. Queen Units to Freedom Units \n'
              '3. Return to the main menu\n'
              '4. Quit like the yella-bellied coward you are')
        inp = int(input('> '))

        match inp:
            case 1:
                f_to_c()
            case 2:
                c_to_f()
            case 3:
                print()
                break
            case 4:
                print('Good riddance, coward...')
                exit()
