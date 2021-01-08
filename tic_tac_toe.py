#!/usr/bin/env python3
from random import randint

play_options = ['rock', 'paper', 'scissors']

computer = play_options[randint(0, 2)]

player = False

while player == False:
    player = input('Rco, paper, Scissors?')
    if player == computer:
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('you lose', computer, 'cover', player)
        else:
            print('you win', player, 'smashes', computer)
    else:
        print('not a valid entry')

    player = False
    computer = play_options[randint(0, 2)]
