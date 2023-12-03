"""
Write a function that takes an integer as input and returns the sum of its digits. e.g. 472 = 13 (4 + 7 + 2)
"""

print('Enter a number with more than 1 digit')
user_input = input('> ')


def sum_of_digit(num):
    # initializes the sum and sets it to 0
    digit_sum = 0
    # casts the number that the user enters into a string for looping
    str_num = str(num)
    # loops through the string and turns each digit into their own thing
    for num in str_num:
        # adds each separate "string" of num to digit_sum, therefore adding each digit
        digit_sum += int(num)
    print(f'The sum of the digits of your number is: {digit_sum}')


sum_of_digit(user_input)
