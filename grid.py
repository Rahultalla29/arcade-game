
import cells
import game_parser
from player import Player



def grid_to_string(grid, player):
    
    dynamic_grid = [] # changes based on player position
    
    # Msg flags
    water_msg = False
    fire_msg = False
    
    
    # Section 1: Conversion of cell objects 
    i = 0 
    while i < len(grid):
        k = 0
        while k < len(grid[i]):
            if (i == player.row and k == player.col) and (type(grid[i][k]) == cells.Water): # If position in grid == position of player
                player.mod_num_water_buckets("+") # Adds water bucket
                dynamic_grid.append(player.display)
                grid[i][k] = cells.Air() # Converts water cell to air cell after being stepped on
                
                water_msg = True
                
            elif (i == player.row and k == player.col) and (type(grid[i][k]) == cells.Fire):
                if player.num_water_buckets > 0: 
                    player.mod_num_water_buckets("-") 
                    dynamic_grid.append(player.display)
                    grid[i][k] = cells.Air()
                    fire_msg = True

                else:
                    
                    dynamic_grid.append(player.display)
                          
                        
            elif (i == player.row and k == player.col): # For position in grid (Air cell) == position of player
                dynamic_grid.append(player.display)

            else:
                dynamic_grid.append(grid[i][k].display) # Add cells as strings to dynamic_grid
                           

            
            k += 1

        i += 1 

    # Section 2: Grid dimensions
    num_row = len(grid)
    len_row = len(grid[0])
    
    output_grid = [] 
    k = 0
    i  = 0
    while i < num_row: 

        temp_ls = []
        k = (i*len_row)
        while k < ((i+1)*len_row) : # Append elements of list for a certain length of row to temporary list (temp_ls)
            temp_ls.append(dynamic_grid[k])
            k +=1
        temp_ls = "".join(temp_ls) # Joins each row to form string and append to final list (output_grid)
        output_grid.append(temp_ls)
        temp_ls = [] # Reset list
        i +=1
    
    # Section 3: Convert grid and specifc message to one string
    if water_msg and player.num_water_buckets == 1:
        string = "\n".join(output_grid) + "\n\nYou have {} water bucket.".format(player.num_water_buckets) + "\n\nThank the Honourable Furious Forest, you've found a bucket of water!"
    elif water_msg:
        string = "\n".join(output_grid) + "\n\nYou have {} water buckets.".format(player.num_water_buckets) + "\n\nThank the Honourable Furious Forest, you've found a bucket of water!"

    elif fire_msg and player.num_water_buckets == 1:
        string = "\n".join(output_grid) + "\n\nYou have {} water bucket.".format(player.num_water_buckets) + "\n\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
    elif fire_msg:
        string = "\n".join(output_grid) + "\n\nYou have {} water buckets.".format(player.num_water_buckets) + "\n\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!"
    
    elif player.num_water_buckets == 1:
        string = "\n".join(output_grid) + "\n\nYou have {} water bucket.".format(player.num_water_buckets) 

    else:
        string = "\n".join(output_grid) + "\n\nYou have {} water buckets.".format(player.num_water_buckets)


    return string
    
    
