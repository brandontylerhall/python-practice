"""
must i even describe what this banger is
"""

x = 0
while x < 100:

    x += 1
    if x % 15 == 0:
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
