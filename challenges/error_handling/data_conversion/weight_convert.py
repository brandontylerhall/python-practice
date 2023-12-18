valid_units = {'1', '2', '3', '4', '5', '6', '7', 'tn', 'kg', 'lb', 'g', 'oz', 'mg'}

result = None


def tons_convert():
    global result
    tn = float(input("\nHow many tons are we converting:\n> "))
    tn_to = input('\nWhat are we converting to:\n'
                  '1. Kilograms (kg)\n'
                  '2. Pounds (lb)\n'
                  '3. Grams (g)\n'
                  '4. Ounces (oz)\n'
                  '5. Milligrams (mg)\n'
                  '> ')
    if tn_to in valid_units:
        match tn_to:
            case '1' | 'kg':
                result = (tn * 907.2)
                print(f'\nYou converted {tn} tons to {result:,.2f} kilograms.\n')
            case '2' | 'lb':
                result = (tn * 2000)
                print(f'\nYou converted {tn} tons to {result:,.2f} pounds.\n')
            case '3' | 'g':
                result = (tn * 907200)
                print(f'\nYou converted {tn} tons to {result:,.2f} grams.\n')
            case '4' | 'oz':
                result = (tn * 32000)
                print(f'\nYou converted {tn} tons to {result:,.2f} ounces.\n')
            case '5' | 'mg':
                result = (tn * 9.072e+8)
                print(f'\nYou converted {tn} tons to {result:,.2f} milligrams.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def kilograms_convert():
    global result
    kg = float(input("\nHow many kilograms are we converting:\n> "))
    kg_to = input('\nWhat are we converting to:\n'
                  '1. Tons (tn)\n'
                  '2. Pounds (lb)\n'
                  '3. Grams (g)\n'
                  '4. Ounces (oz)\n'
                  '5. Milligrams (mg)\n'
                  '> ')
    if kg_to in valid_units:
        match kg_to:
            case '1' | 'tn':
                result = (kg / 907.2)
                print(f'\nYou converted {kg} kilograms to {result:,.2f} tons.\n')
            case '2' | 'lb':
                result = (kg * 2.205)
                print(f'\nYou converted {kg} kilograms to {result:,.2f} pounds.\n')
            case '3' | 'g':
                result = (kg * 1000)
                print(f'\nYou converted {kg} kilograms to {result:,.2f} grams.\n')
            case '4' | 'oz':
                result = (kg * 35.274)
                print(f'\nYou converted {kg} kilograms to {result:,.2f} ounces.\n')
            case '5' | 'mg':
                result = (kg * 1e+6)
                print(f'\nYou converted {kg} kilograms to {result:,.2f} milligrams.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def pounds_convert():
    global result
    lb = float(input("\nHow many pounds are we converting:\n> "))
    lb_to = input('\nWhat are we converting to:\n'
                  '1. Tons (tn)\n'
                  '2. Kilograms (lb)\n'
                  '3. Grams (g)\n'
                  '4. Ounces (oz)\n'
                  '5. Milligrams (mg)\n'
                  '> ')
    if lb_to in valid_units:
        match lb_to:
            case '1' | 'tn':
                result = (lb / 2000)
                print(f'\nYou converted {lb} pounds to {result:,.2f} tons.\n')
            case '2' | 'kg':
                result = (lb / 2.205)
                print(f'\nYou converted {lb} pounds to {result:,.2f} kilograms.\n')
            case '3' | 'g':
                result = (lb / 453.6)
                print(f'\nYou converted {lb} pounds to {result:,.2f} grams.\n')
            case '4' | 'oz':
                result = (lb * 16)
                print(f'\nYou converted {lb} pounds to {result:,.2f} ounces.\n')
            case '5' | 'mg':
                result = (lb * 453600)
                print(f'\nYou converted {lb} pounds to {result:,.2f} milligrams.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def grams_convert():
    global result
    m = float(input("\nHow many grams are we converting:\n> "))
    m_to = input('\nWhat are we converting to:\n'
                 '1. Tons (tn)\n'
                 '2. Kilograms (lb)\n'
                 '3. Pounds (lb)\n'
                 '4. Ounces (oz)\n'
                 '5. Milligrams (mg)\n'
                 '> ')
    if m_to in valid_units:
        match m_to:
            case '1' | 'tn':
                result = (m / 907200)
                print(f'\nYou converted {m} grams to {result:,.2f} tons.\n')
            case '2' | 'kg':
                result = (m / 1000)
                print(f'\nYou converted {m} grams to {result:,.2f} kilograms.\n')
            case '3' | 'lb':
                result = (m / 453.6)
                print(f'\nYou converted {m} grams to {result:,.2f} pounds.\n')
            case '4' | 'oz':
                result = (m / 28.35)
                print(f'\nYou converted {m} grams to {result:,.2f} ounces.\n')
            case '5' | 'mg':
                result = (m * 1000)
                print(f'\nYou converted {m} grams to {result:,.2f} milligrams.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def ounces_convert():
    global result
    oz = float(input("\nHow many ounces are we converting:\n> "))
    oz_to = input('\nWhat are we converting to:\n'
                  '1. Tons (tn)\n'
                  '2. Kilograms (oz)\n'
                  '3. Pounds (lb)\n'
                  '4. Grams (g)\n'
                  '5. Milligrams (mg)\n'
                  '> ')
    if oz_to in valid_units:
        match oz_to:
            case '1' | 'tn':
                result = (oz * 32000)
                print(f'\nYou converted {oz} ounces to {result:,.2f} tons.\n')
            case '2' | 'kg':
                result = (oz / 35.274)
                print(f'\nYou converted {oz} ounces to {result:,.2f} kilograms.\n')
            case '3' | 'lb':
                result = (oz / 16)
                print(f'\nYou converted {oz} ounces to {result:,.2f} pounds.\n')
            case '4' | 'g':
                result = (oz * 28.35)
                print(f'\nYou converted {oz} ounces to {result:,.2f} grams.\n')
            case '5' | 'mg':
                result = (oz * 28350)
                print(f'\nYou converted {oz} ounces to {result:,.2f} milligrams.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def milligrams_convert():
    global result
    mg = float(input("\nHow many milligrams are we converting:\n> "))
    mg_to = input('\nWhat are we converting to:\n'
                  '1. Tons (tn)\n'
                  '2. Kilograms (oz)\n'
                  '3. Pounds (lb)\n'
                  '4. Grams (g)\n'
                  '5. Ounces (oz)\n'
                  '> ')
    if mg_to in valid_units:
        match mg_to:
            case '1' | 'tn':
                result = (mg / 9.072e+8)
                print(f'\nYou converted {mg} milligrams to {result:,.2f} tons.\n')
            case '2' | 'kg':
                result = (mg / 1e+6)
                print(f'\nYou converted {mg} milligrams to {result:,.2f} kilograms.\n')
            case '3' | 'lb':
                result = (mg / 453600)
                print(f'\nYou converted {mg} milligrams to {result:,.2f} pounds.\n')
            case '4' | 'g':
                result = (mg / 1000)
                print(f'\nYou converted {mg} milligrams to {result:,.2f} grams.\n')
            case '5' | 'oz':
                result = (mg / 28350)
                print(f'\nYou converted {mg} milligrams to {result:,.2f} ounces.\n')
    else:
        print('\nInvalid option. Please try again.\n')


def weight_convert():
    while True:
        print('What do you want to convert:\n'
              '1. Tons (tn)\n'
              '2. Kilograms (kg)\n'
              '3. Pounds (lb)\n'
              '4. Grams (g)\n'
              '5. Ounces (oz)\n'
              '6. Milligrams (mg)\n'
              '7. Main menu\n'
              '8. Quit')
        unit = input('> ')

        if unit in valid_units:
            match unit:
                case '1' | 'tn':
                    tons_convert()
                case '2' | 'kg':
                    kilograms_convert()
                case '3' | 'lb':
                    pounds_convert()
                case '4' | 'g':
                    grams_convert()
                case '5' | 'oz':
                    ounces_convert()
                case '6' | 'mg':
                    milligrams_convert()
                case '7':
                    break
                case '8':
                    exit()
        else:
            print('Invalid input. Please enter a valid number or unit.\n')
