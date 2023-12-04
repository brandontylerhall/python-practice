"""
    Write a function that generates the Collatz sequence for a given starting number.
    The sequence should end when it reaches 1.
"""


def collatz(num):
    print(num)
    if num == 1:
        return
    if num % 2 == 0:
        num //= 2
        collatz(num)
    elif num % 2 == 1:
        num = (num * 3) + 1
        collatz(num)


inp = int(input('Enter a number: '))
collatz(inp)
