"""
    Write a function that takes a string as input and returns the count of vowels in it.
"""

user_inp = input('Enter a word and I will count how many vowels there are inside of it \n')

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0


def vowel_count(inp):
    # used global to indicate i'm using the global variable count instead of creating a local one
    global count
    for v in inp:
        # iterates through each character in the vowel list
        if v in vowels:
            count += 1
    return count


result = vowel_count(user_inp)
print(f'There are {result} vowels in "{user_inp}."')
