"""
    Write a function that generates the Collatz sequence for a given starting number.
    The sequence should end when it reaches 1.
"""

inp = 9

def collatz(num):
    if num % 2 == 0:
        num /= 2
        print(num)
    if num % 3 == 0:
        num = (num * 3) + 1
        print(num)


while inp > 1:
    collatz(inp)