from temp_convert import temp_convert
from length_convert import length_convert


def main():
    while True:
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
            case '2':
                print()
                length_convert()
            case '4':
                exit()


if __name__ == '__main__':
    main()
