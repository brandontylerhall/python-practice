from temp_convert import temp_convert


def main():
    inp = input('What do you want to convert:\n'
                '1. Temperature\n'
                '2. Weight\n'
                '3. Length\n'
                '4. Quit\n'
                '> ').lower()
    match inp:
        case '1':
            print()
            temp_convert()
        case '4':
            exit()


main()
