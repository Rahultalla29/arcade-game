class Player:
    def __init__(self,display):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0
    def mod_num_water_buckets(self,action):# To modify number of water buckets
        valid_in = ["-","+"] 
        if action not in valid_in:
            raise Exception("Please enter - or + ")
        if action == "-":
            self.num_water_buckets -= 1
        if action == "+":
            self.num_water_buckets += 1
        

    
    def move(self, move): # Move modificaton
        if move == "w" :
            self.row -= 1
        if move == "a" :
            self.col -= 1
        if move == "d":
            self.col += 1
        if move == 's':
            self.row += 1
        if move == 'e':
            pass
        

    