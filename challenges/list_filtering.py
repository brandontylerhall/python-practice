"""
    Write a function that takes a list of numbers and returns a new list containing only the even numbers.
"""


def list_filter(inp):
    even_list = []
    # turns input into a list because of split.() and removes commas because of
    # .replace('thing to remove', 'thing to replace with') to be able to iterate through list
    # furthermore, in list comprehension (which we just did) you must include the variable which will be in the new list
    # e.g. num for num in inp = a new value which comprises "num"s.
    # the second num is simply the iterable variable
    num_list = [int(num) for num in inp.replace(',', '').split()]
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


user_in = input('Enter a bunch of numbers, even and odd, separated by a comma (e.g. 1, 6, 2, 18...): ')
new_list = list_filter(user_in)
print(f'Your new and improved set of numbers with ONLY the evens is: {new_list}')
