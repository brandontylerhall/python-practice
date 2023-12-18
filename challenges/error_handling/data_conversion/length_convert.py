valid_units = {'1', '2', '3', '4', '5', '6', '7', 'mi', 'km', 'ft', 'm', 'in', 'cm'}

result = None


def miles_convert():
    global result
    mi = int(input("How many miles are we converting:\n> "))
    mi_to = input('What are we converting to:\n'
                  '1. Kilometers (km)\n'
                  '2. Feet (ft)\n'
                  '3. Meters (m)\n'
                  '4. Inches (in)\n'
                  '5. Centimeters (cm)\n'
                  '> ')
    match mi_to:
        case '1' | 'km':
            result = round(mi * 1.609)
        case '2' | 'ft':
            result = round(mi * 5280)
        case '3' | 'm':
            result = round(mi * 1609.34)
        case '4' | 'in':
            result = round(mi * 63360)
        case '5' | 'cm':
            result = round(mi * 160934)
    print(f'You converted {mi} miles to {result} {mi_to}')


def kilometers_convert():
    pass


def feet_convert():
    pass


def meters_convert():
    pass


def inches_convert():
    pass


def centimeters_convert():
    pass


def length_convert():
    while True:
        print('What do you want to convert:\n'
              '1. Miles (mi)\n'
              '2. Kilometers (km)\n'
              '3. Feet (ft)\n'
              '4. Meters (m)\n'
              '5. Inches (in)\n'
              '6. Centimeters (cm)\n'
              '7. Main menu')
        unit = input('> ')

        if unit in valid_units:
            match unit:
                case '1' | 'mi':
                    miles_convert()
                case '2' | 'km':
                    pass
                case '3' | 'ft':
                    pass
                case '4' | 'm':
                    pass
                case '5' | 'in':
                    pass
                case '6' | 'cm':
                    pass
                case '7':
                    break
        else:
            print('Invalid input. Please enter a valid number or unit.')


length_convert()
