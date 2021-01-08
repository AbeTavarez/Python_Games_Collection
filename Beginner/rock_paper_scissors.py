#!/usr/bin/env python3
from random import randint

# List of Moves
game_moves = ['rock', 'paper', 'scissors']

# Computer Init
computer = game_moves[randint(0, 2)]

# Player Init
player = False

while player == False:
  # * While the player is equals to False  loop will run
    # Assigns player's move from input
    player = input('=== Ready? Choose: rock, paper or scissor ? ===')

    # *** If Player and Computer choose the same move *************
    if player == computer:
        print('=== Is a Tie. Go again! ===')

    # *** If Player chooses 'rock' ********************************
    elif player == 'rock':
        # Checks if computer move is 'paper'
        if computer == 'paper':
            print('x:::(Oh noo You got beat by a bot!):::x',
                  computer, 'covers', player)
        else:
            # If the computer didnt pick 'paper' then player wins
            print('+++Nice move. You win!+++',
                  player, 'smashes', computer)

    # *** If Player chooses 'paper' ********************************
    elif player == 'paper':
        # Checks if computer move is 'scissor'
        if computer == 'scissor':
            print('x:::(Oh noo You got beat by a bot!):::x',
                  computer, 'slices', player)
        else:
            # If the computer didnt pick 'scissor' then player wins
            print('+++Nice move. You win!+++',
                  player, 'covers', computer)

    # *** If Player chooses 'scissor' ******************************
    elif player == 'scissor':
        # Checks if computer move is 'rock'
        if computer == 'rock':
            print('x:::(Oh noo You got beat by a bot!):::x',
                  computer, 'smashes', player)
        else:
            # If the computer didnt pick 'scissor' then player wins
            print('+++Nice move. You win!+++',
                  player, 'slices', computer)
    else:
        # If the player didnt pick [rock, paper nor scissor]
        # then this message is printed
        # and the loops starts again.
        print('Please choose [rock, paper or scissor] Try again!')
    # We are stiil inside the loop here
    # The values for the player and the computer gets resetted
    player = False  # default value
    computer = game_moves[randint(0, 2)]  # random move from game_moves list
