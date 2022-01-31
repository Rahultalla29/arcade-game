# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)



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
            if (grid[i][k] == "X" ): #Find X
                row = int(i)
                col = int(k)
                return row,col

            k += 1
        i += 1 

def solve(filename):
    grid = read_lines(filename)
    start_pos = some(grid)
    x = start_pos[0]
    y = start_pos[1]
    ls = ["u","d","r","l"]
    pass
# Base Cases
# # if (x,y outside maze) return false
# # if (x,y is goal) return true
# # if (x,y is wall) return false
# # if (x,y is air) return true

def solve(mode):
    pass


if __name__ == "__main__":
    solution_found = False
    if solution_found:
        pass
        # Print your solution...
    else:
        print("There is no possible path.")


