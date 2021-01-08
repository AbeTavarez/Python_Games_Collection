#!/usr/bin/env python3
from random import randint

game_moves = ['rock', 'paper', 'scissors']

computer = game_moves[randint(0, 2)]

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
    computer = game_moves[randint(0, 2)]
