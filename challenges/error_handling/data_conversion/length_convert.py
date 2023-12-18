valid_units = {'1', '2', '3', '4', '5', '6', '7', 'mi', 'km', 'ft', 'm', 'in', 'cm'}

result = None


def miles_convert():
    global result
    mi = float(input("\nHow many miles are we converting:\n> "))
    mi_to = input('\nWhat are we converting to:\n'
                  '1. Kilometers (km)\n'
                  '2. Feet (ft)\n'
                  '3. Meters (m)\n'
                  '4. Inches (in)\n'
                  '5. Centimeters (cm)\n'
                  '> ')
    if mi_to in valid_units:
        match mi_to:
            case '1' | 'km':
                result = (mi * 1.609)
                print(f'\nYou converted {mi} miles to {result:,.2f} kilometers.\n')
            case '2' | 'ft':
                result = (mi * 5280)
                print(f'\nYou converted {mi} miles to {result:,.2f} feet.\n')
            case '3' | 'm':
                result = (mi * 1609.34)
                print(f'\nYou converted {mi} miles to {result:,.2f} meters.\n')
            case '4' | 'in':
                result = (mi * 63360)
                print(f'\nYou converted {mi} miles to {result:,.2f} inches.\n')
            case '5' | 'cm':
                result = (mi * 160934)
                print(f'\nYou converted {mi} miles to {result:,.2f} centimeters.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def kilometers_convert():
    global result
    km = float(input("\nHow many kilometers are we converting:\n> "))
    km_to = input('\nWhat are we converting to:\n'
                  '1. Miles (mi)\n'
                  '2. Feet (ft)\n'
                  '3. Meters (m)\n'
                  '4. Inches (in)\n'
                  '5. Centimeters (cm)\n'
                  '> ')
    if km_to in valid_units:
        match km_to:
            case '1' | 'mi':
                result = (km * 0.621)
                print(f'\nYou converted {km} kilometers to {result:,.2f} miles.\n')
            case '2' | 'ft':
                result = (km * 3280.84)
                print(f'\nYou converted {km} kilometers to {result:,.2f} feet.\n')
            case '3' | 'm':
                result = (km * 1000)
                print(f'\nYou converted {km} kilometers to {result:,.2f} meters.\n')
            case '4' | 'in':
                result = (km * 39370.1)
                print(f'\nYou converted {km} kilometers to {result:,.2f} inches.\n')
            case '5' | 'cm':
                result = (km * 10000)
                print(f'\nYou converted {km} kilometers to {result:,.2f} centimeters.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def feet_convert():
    global result
    ft = float(input("\nHow many feet are we converting:\n> "))
    ft_to = input('\nWhat are we converting to:\n'
                  '1. Miles (mi)\n'
                  '2. Kilometers (ft)\n'
                  '3. Meters (m)\n'
                  '4. Inches (in)\n'
                  '5. Centimeters (cm)\n'
                  '> ')
    if ft_to in valid_units:
        match ft_to:
            case '1' | 'mi':
                result = (ft / 5280)
                print(f'\nYou converted {ft} feet to {result:,.2f} miles.\n')
            case '2' | 'km':
                result = (ft / 3281)
                print(f'\nYou converted {ft} feet to {result:,.2f} kilometers.\n')
            case '3' | 'm':
                result = (ft / 3.281)
                print(f'\nYou converted {ft} feet to {result:,.2f} meters.\n')
            case '4' | 'in':
                result = (ft * 12)
                print(f'\nYou converted {ft} feet to {result:,.2f} inches.\n')
            case '5' | 'cm':
                result = (ft * 30.48)
                print(f'\nYou converted {ft} feet to {result:,.2f} centimeters.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def meters_convert():
    global result
    m = float(input("\nHow many meters are we converting:\n> "))
    m_to = input('\nWhat are we converting to:\n'
                 '1. Miles (mi)\n'
                 '2. Kilometers (ft)\n'
                 '3. Feet (ft)\n'
                 '4. Inches (in)\n'
                 '5. Centimeters (cm)\n'
                 '> ')
    if m_to in valid_units:
        match m_to:
            case '1' | 'mi':
                result = (m / 1609)
                print(f'\nYou converted {m} meters to {result:,.2f} miles.\n')
            case '2' | 'km':
                result = (m / 1000)
                print(f'\nYou converted {m} meters to {result:,.2f} kilometers.\n')
            case '3' | 'ft':
                result = (m * 3.281)
                print(f'\nYou converted {m} meters to {result:,.2f} feet.\n')
            case '4' | 'in':
                result = (m * 39.37)
                print(f'\nYou converted {m} meters to {result:,.2f} inches.\n')
            case '5' | 'cm':
                result = (m * 100)
                print(f'\nYou converted {m} meters to {result:,.2f} centimeters.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def inches_convert():
    global result
    inch = float(input("\nHow many inches are we converting:\n> "))
    inch_to = input('\nWhat are we converting to:\n'
                    '1. Miles (mi)\n'
                    '2. Kilometers (in)\n'
                    '3. Feet (ft)\n'
                    '4. Meters (m)\n'
                    '5. Centimeters (cm)\n'
                    '> ')
    if inch_to in valid_units:
        match inch_to:
            case '1' | 'mi':
                result = (inch * 63360)
                print(f'\nYou converted {inch} inches to {result:,.2f} miles.\n')
            case '2' | 'km':
                result = (inch / 39370)
                print(f'\nYou converted {inch} inches to {result:,.2f} kilometers.\n')
            case '3' | 'ft':
                result = (inch * 12)
                print(f'\nYou converted {inch} inches to {result:,.2f} feet.\n')
            case '4' | 'm':
                result = (inch / 39.37)
                print(f'\nYou converted {inch} inches to {result:,.2f} meters.\n')
            case '5' | 'cm':
                result = (inch * 2.54)
                print(f'\nYou converted {inch} inches to {result:,.2f} centimeters.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def centimeters_convert():
    global result
    cm = float(input("\nHow many centimeters are we converting:\n> "))
    cm_to = input('\nWhat are we converting to:\n'
                  '1. Miles (mi)\n'
                  '2. Kilometers (in)\n'
                  '3. Feet (ft)\n'
                  '4. Meters (m)\n'
                  '5. Inches (in)\n'
                  '> ')
    if cm_to in valid_units:
        match cm_to:
            case '1' | 'mi':
                result = (cm / 160900)
                print(f'\nYou converted {cm} centimeters to {result:,.2f} miles.\n')
            case '2' | 'km':
                result = (cm / 100000)
                print(f'\nYou converted {cm} centimeters to {result:,.2f} kilometers.\n')
            case '3' | 'ft':
                result = (cm / 30.48)
                print(f'\nYou converted {cm} centimeters to {result:,.2f} feet.\n')
            case '4' | 'm':
                result = (cm / 100)
                print(f'\nYou converted {cm} centimeters to {result:,.2f} meters.\n')
            case '5' | 'in':
                result = (cm / 2.54)
                print(f'\nYou converted {cm} centimeters to {result:,.2f} inches.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def length_convert():
    while True:
        print('What do you want to convert:\n'
              '1. Miles (mi)\n'
              '2. Kilometers (km)\n'
              '3. Feet (ft)\n'
              '4. Meters (m)\n'
              '5. Inches (in)\n'
              '6. Centimeters (cm)\n'
              '7. Main menu\n'
              '8. Quit')
        unit = input('> ')

        if unit in valid_units:
            match unit:
                case '1' | 'mi':
                    miles_convert()
                case '2' | 'km':
                    kilometers_convert()
                case '3' | 'ft':
                    feet_convert()
                case '4' | 'm':
                    meters_convert()
                case '5' | 'in':
                    inches_convert()
                case '6' | 'cm':
                    centimeters_convert()
                case '7':
                    break
                case '8':
                    exit()
        else:
            print('Invalid input. Please enter a valid number or unit.\n')
