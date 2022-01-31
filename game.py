from game_parser import read_lines
from grid import grid_to_string
from player import Player
import cells


class Game:
    player1 = Player("A")
    def __init__(self, filename):
        self.filename = filename  
        self.moves_list = []
        self.num_of_moves = None
        self.game_state = True # Used to deteremine when game ends
        self.game_board = read_lines(filename) 
        
        
    def initial_player_position(filename,player): # Initial output
        original_grid = read_lines(filename)   

        i = 0 
        while i < len(original_grid):
            k = 0
            while k < len(original_grid[i]):
                if (original_grid[i][k].display == "X" ): # If position in grid == position of player
                    player.row = int(i)
                    player.col = int(k)
                    break
                    
                
                k += 1

            i += 1 
        return grid_to_string(original_grid,player)
    
    def game_move(self,player,step): # Gets move and modifies returned grid accordingly
        
        if len(self.moves_list) < 0 :
            self.moves_list.append(step)
        else:
            self.moves_list.append(" {}".format(step))

        
        player.move(step) # Makes prelimianry move

        # Section 1: Set teleport position of player
        teleport_pads  = ["1","2","3","4","5","6","7","8","9"]
        if self.game_board[player.row][player.col].display in teleport_pads:
            count1 = 0
            while count1 < len(self.game_board):
                count2 = 0
                while count2 < len(self.game_board[count1]):

                    game_pad_equal_player_pad = (self.game_board[count1][count2].display == self.game_board[player.row][player.col].display)
                    game_pad_position_not_equal_player = ((player.row != count1) or (player.col != count2))

                    if game_pad_equal_player_pad and game_pad_position_not_equal_player :
                        player.row = count1
                        player.col = count2
                        return grid_to_string(self.game_board,player) + "\n\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."
                    
                    count2 += 1
                
                count1 +=1
        
        # Section 2: Wall and walking out of boundaries 
        player_outside_row_limit = player.row > (len(self.game_board)) or player.row < 0
        player_outside_col_limit = player.col > (len(self.game_board[0])) or player.col < 0


        
        if self.game_board[player.row][player.col].display == "*" or player_outside_col_limit:
            del self.moves_list[-1]
            if step == "w":
                player.move("s")
            if step == "s":
                player.move("w")
            if step == "a":
                player.move ("d")
            if step == "d":
                player.move("a")
            return grid_to_string(self.game_board,player) + "\n\nYou walked into a wall. Oof!"
        
        # Section 3: Moves messages
        self.num_of_moves = len(self.moves_list)
        if self.num_of_moves == 1:
            num_moves_msg = "\n\nYou made {} move.".format(self.num_of_moves)
            moves_made_msg = "\nYour move:"+ ",".join(self.moves_list)
        else:
            num_moves_msg = "\n\nYou made {} moves.".format(self.num_of_moves)
            moves_made_msg = "\nYour moves:"+ ",".join(self.moves_list)

        # Section 4: Win case 
        if self.game_board[player.row][player.col].display == "Y" or player_outside_row_limit:
            
            win_msg = "\n\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the"\
            " Honourable Furious Forest Throne, restoring your hometown back to its former"\
            " glory of rainbow and sunshine! Peace reigns over the lands." 
            win_graphic = "\n\n=====================\n====== YOU WIN! =====\n====================="
            self.game_state = False
            
            return grid_to_string(self.game_board,player) + win_msg + num_moves_msg + moves_made_msg + win_graphic
        
        # Section 5: Lose case due to fire
        if self.game_board[player.row][player.col].display == "F" and (player.num_water_buckets == 0):
            
            lose_msg = "\n\n\nYou step into the fires and watch your dreams disappear :(.\n\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of" \
                " ash and is scattered to the winds by the next storm... You have been roasted."
            lose_graphic = "\n\n=====================\n===== GAME OVER =====\n====================="
            self.game_state = False
            
            return grid_to_string(self.game_board,player) + lose_msg + num_moves_msg + moves_made_msg + lose_graphic

        return grid_to_string(self.game_board,player)

    def get_grid(self,player): # Getter method for grid and current player position
        return grid_to_string(self.game_board,player)

        
