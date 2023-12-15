def length_convert():
    valid_units = {'1', '2', '3', '4', '5', '6', '7', 'mi', 'km', 'ft', 'm', 'in', 'cm'}

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
                    pass
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
