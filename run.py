from game import Game

import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 run.py <filename> [play]")
    exit()

filename = str(sys.argv[1])
current_game = Game(filename) # Initalise Game class

# Premliminary grid output
print(Game.initial_player_position(filename,Game.player1)) 


want_to_play = True # Game state flag

valid_moves = ['w','a','s','d','e','q']
while want_to_play:
    in_move = input("\nInput a move: ")
    in_move = in_move.lower() #Accounts for uppercase
    
    if in_move == 'q':
        print("\nBye!")
        quit()

    elif in_move in valid_moves:
        
        print(current_game.game_move(Game.player1,in_move))
        want_to_play = current_game.game_state # Changes game state based on player position
        

    elif current_game.num_of_moves == None:
        print(Game.initial_player_position(filename,Game.player1)) 
        print("\nPlease enter a valid move (w, a, s, d, e, q).")

    else:
        print(current_game.get_grid(Game.player1)) # Invalid input prompt grid with previous player position
        print("\nPlease enter a valid move (w, a, s, d, e, q).")
        
    



