"""
    Write a function that takes a string as input and counts the number of vowels and consonants.
"""
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
              'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
count_c = 0
count_v = 0

user_in = input('Enter a word or phrase and I will count the amount of consonants '
                'and vowels that are in that word or phrase: \n')


def count_cv(inp):
    global count_c
    global count_v
    for char in inp:
        if char in consonants:
            count_c += 1
        if char in vowels:
            count_v += 1
    return count_c, count_v


result = count_cv(user_in)
if len(user_in) <= 15:
    print(f'There are {count_c} consonants and {count_v} vowels in {user_in}')
else:
    print(f'There are {count_c} consonants and {count_v} vowels in your word or phrase')
