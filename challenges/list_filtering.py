"""
    Write a function that takes a list of numbers and returns a new list containing only the even numbers.
"""
# v1.0
"""
    def list_filter(inp, even=True):
        # 
        #     turns input into a list because of split.() and removes commas because of
        #     .replace('thing to remove', 'thing to replace with') to be able to iterate through list
        #     furthermore, in list comprehension (which we just did) you must include the variable 
        #     which will be in the new list
        #     e.g. num for num in inp = a new value which comprises "num"s.
        #     the second num is simply the iterable variable
        # 
        inp_list = [int(num) for num in inp.replace(',', '').split()]
        even_odd_list = [num for num in inp_list if num % 2 == 0] if even else [num for num in inp_list if num % 2 == 1]
        return even_odd_list
    
    
    user_in = input('Enter a bunch of numbers, even and odd, separated by a comma (e.g. 1, 6, 2, 18...): ')
    filter_opt = input('Would you like to filter your list to get the evens (yes/no): ').lower() == 'yes'
    
    new_list = list_filter(user_in, filter_opt)
    print(f'Your new and improved set of numbers with ONLY the evens is: {new_list}')
"""
# v2.0
"""
    Write a function that takes a list of numbers and returns a new list containing only the even numbers.
"""


def list_filter(inp, even=True):
    inp_list = [int(num) for num in inp.replace(',', '').split()]
    filtered_list = [num for num in inp_list if num % 2 == 0] if even else [num for num in inp_list if num % 2 == 1]
    return filtered_list


user_in = input('Enter a bunch of numbers, even and odd, separated by a comma and space (e.g. 1, 19, 55, 6812...): ')
user_opt = input('Do you want to sort by even or odd numbers: ').lower()

ans = bool
if user_opt == 'even':
    ans = True
elif user_opt == 'odd':
    ans = False

new_list = list_filter(user_in, ans)
print(f'Your new set of {user_opt} numbers is: {new_list}')
