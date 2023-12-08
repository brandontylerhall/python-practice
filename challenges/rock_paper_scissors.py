"""
    Write a simple text-based Rock, Paper, Scissors game where the user can play against the computer.
"""
from random import choice


def rps(inp, cpu):
    if inp == cpu:
        return f'You both chose {inp}! It\'s a tie! Choose again! \n'

    elif (inp == 'rock' and cpu == 'scissors' or
          inp == 'scissors' and cpu == 'paper' or
          inp == 'paper' and cpu == 'rock'):
        return f'The computer chose {cpu}! You win!'

    elif (inp == 'paper' and cpu == 'scissors' or
          inp == 'rock' and cpu == 'paper' or
          inp == 'scissors' and cpu == 'rock'):
        return f'The computer chose {cpu}! You lose!'


def play_rps():
    moves = ['rock', 'paper', 'scissors']

    while True:
        user_in = input('Rock, paper, or scissors? \n')
        cpu_move = choice(moves)

        result = rps(user_in, cpu_move)
        print(result)

        # checks to see if the words win or lose are in the return statement
        # because if they are, that means someone won and the game ends
        if 'win' in result or 'lose' in result:
            break


play_rps()
