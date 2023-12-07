def unique_filter(inp):
    # uses list comprehension to remove any duplicates in the input and return a list
    unique = set(char for char in inp.replace(',', '').split())
    return unique


user_in = input('Enter a bunch of stuff, separated by a comma. '
                'I will return a list with all of the unique characters. \n')

new_list = unique_filter(user_in)
# sorted() converts the set to a sorted list
sorted_list = sorted(new_list)
# ", ".join(map(str, sorted_list)) joins the elements into a comma-separated string
print(f'your unique values are: {", ".join(map(str, sorted_list))}')
