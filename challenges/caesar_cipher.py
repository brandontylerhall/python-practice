"""
    Implement a Caesar cipher function that encrypts a given string
    by shifting each letter by a certain number of positions in the alphabet.
"""

user_in = input('Enter the word or phrase you wish to encrypt: \n')
shift = int(input('How many letters over do you want to shift your phrase: \n'))
left_right = input(f'Do you want to shift the characters in your phrase {shift} to the left or to the right \n')


def caesar(inp, l_r, opt):
    if l_r == 'left':
        return ''.join(chr((ord(char) - 97 - opt) % 26 + 97) for char in inp)
    elif l_r == 'right':
        return ''.join(chr((ord(char) - 97 + opt) % 26 + 97) for char in inp)


new_phrase = caesar(user_in, left_right, shift)
print(f'Your new phrase is: {new_phrase} \n'
      f'The characters were shifted {shift} times')
