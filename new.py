# **X***
# *    *
# * ** *
# *    *
# *    *
# ****Y*

# [['*', '*', 'X', '*', '*', '*'], 

filename = "board_medium.txt"

def read_lines(filename):
    try:
    
        f = open(filename,"r")
        lines = f.readlines()
        f.close() 
        filtered_contents = []
        for line in lines:
            line = line.rstrip("\n")
            filtered_contents.append(list(line))  #read lines converted to cells objects in list of lists
        return filtered_contents
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()

def some(grid):

    i = 0 
    while i < len(grid):
        k = 0
        while k < len(grid[i]):
            if (grid[i][k] == "X" ): #if position in grid == position of player
                row = int(i)
                col = int(k)
                return row,col

            k += 1
        i += 1 
def solve(filename):
    grid = read_lines(filename)
    start_pos = some(grid)
    row = start_pos[0]
    col = start_pos[1]
    return row,col
print(solve(filename))