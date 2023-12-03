"""
Write a function that checks if a given word or phrase is a palindrome.
"""

palindrome_to_be = input('enter a word to check if it\'s a palindrome: ')

# from GPT:
# The first : specifies the start of the slice (default is the beginning).
# The second : specifies the end of the slice (default is the end).
# The -1 as the third argument represents the step. A step of -1 means to iterate backward.
# So, [::-1] essentially means:
#
# Start from the end of the sequence.
# Go until the beginning of the sequence.
# Step backward by one element at a time.

if palindrome_to_be == palindrome_to_be[::-1]:
    print('yep')
else:
    print('nope')
