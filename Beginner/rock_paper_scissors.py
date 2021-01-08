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

    # Checks if player and Computer choose the same move
    if player == computer:
        print('=== Is a Tie. Go again! ===')
    # Player chooses 'rock'
    elif player == 'rock':
        # Checks if computer move is 'paper'
        if computer == 'paper':
            print('x:::(Oh noo You got beat by a bot!):::x',
                  computer, 'covers', player)
        else:
            # If the computer didnt pick 'paper' then player wins
            print('+++Nice move. You win!+++',
                  player, 'smashes', computer)
    else:
        # If the player didnt pick [rock, paper nor scissor]
        # then this message is printed
        # and the loops starts again.
        print('Please choose [rock, paper or scissor] Try again!')
    # We are stiil inside the loop here
    # The values for the player and the computer gets resetted
    player = False  # default value
    computer = game_moves[randint(0, 2)]  # random move from game_moves list
