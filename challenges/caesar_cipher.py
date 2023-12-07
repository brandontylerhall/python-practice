"""
    Implement a Caesar cipher function that encrypts a given string
    by shifting each letter by a certain number of positions in the alphabet.
"""


def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():  # check if the character is a letter
            if char.isupper():  # check if the character is uppercase
                # ord() takes a single unicode letter and returns the numerical value of that character
                # e.g. ord('a') returns 97
                result += chr((ord(char) - ord('A' if direction == 'left' else 'a') - shift) % 26 + ord('A'))
            else:  # does this if lowercase
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # if character is not a letter (e.g. space) it adds it to the string unchanged
            result += char
    return result


user_in = input('Enter the word or phrase you wish to encrypt: \n')
encrypt = int(input('How many letters over do you want to shift your phrase: \n'))
left_right = input('Do you want to shift the characters in your phrase to the left or to the right: \n')

new_phrase = caesar_cipher(user_in, encrypt, left_right)
print(f'Your new phrase is: {new_phrase}\n'
      f'The characters were shifted {encrypt} times to the {left_right}.')
