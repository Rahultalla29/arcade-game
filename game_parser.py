from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

"""Read in a file, process them using parse(),
and return the contents as a list of list of cells."""

def read_lines(filename):
    try:
    
        f = open(filename,"r")
        lines = f.readlines()
        f.close() 
        filtered = parse(lines)  #read lines converted to cells objects in list of lists
        return filtered
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()
    



def parse(lines):

    # Section 1: Test validitity of input list
    if type(lines) != list:
        raise TypeError("Expected list")
    
    i = 0
    for elem in lines:
        if type(lines[i]) != str:
            raise TypeError("Expected list of strings")
        i +=1

    i = 0
    x_count = 0
    y_count = 0 
    teleport_pads = [] # Section 2: All valid teleport pads encountered 
    
    while i < len(lines):
        
        ls = list(lines)
        string = ls[i]
        
        x_count += string.count("X")
        y_count += string.count("Y")
        
        k = 0
        while k < len(string): # Section 3: Testing existence of unvalid letters in config. file
            valid_letters = ["A"," ","X","Y","*","1","2","3","4","5","6","7","8","9","W","F","\n"]
            
            if string[k] not in valid_letters:
                raise  ValueError("Bad letter in configuration file: {}.".format(string[k]))
            if string[k].isdigit() and (string[k] in valid_letters) :
                teleport_pads.append(string[k])


            k += 1
    
        i+=1

    # Section 4: Occurence of X and Y test
    if x_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(str(x_count))) 
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(str(y_count))) 
    
    # Section 5: Teleport pad matching pair test
    teleport_pads_counts = [[x,teleport_pads.count(x)] for x in set(teleport_pads)]
    
    pad_counter = 0
    while pad_counter < len(teleport_pads_counts):
        if teleport_pads_counts[pad_counter][1] != 2:
            pad_number = str(teleport_pads_counts[pad_counter][0])
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(pad_number))
        pad_counter += 1
    
    # Section 6: Removing escape character from input list of strings
    filtered_contents = []
    for line in lines:
        line = line.rstrip("\n")
        filtered_contents.append(list(line))

    # Section 7: Conversion of strings to appropriate class objects
    ls_index = 0 
    while ls_index < len(ls):
        
        inner_ls_index = 0
        while inner_ls_index < len(filtered_contents[ls_index]):
            
            if filtered_contents[ls_index][inner_ls_index] == "X": 
                filtered_contents[ls_index][inner_ls_index] = Start()
            
            elif filtered_contents[ls_index][inner_ls_index] == "Y":
                filtered_contents[ls_index][inner_ls_index] = End()
            
            elif filtered_contents[ls_index][inner_ls_index] == "*":
                filtered_contents[ls_index][inner_ls_index] = Wall()
            
            elif filtered_contents[ls_index][inner_ls_index] == " ":
                filtered_contents[ls_index][inner_ls_index] = Air()
            
            elif filtered_contents[ls_index][inner_ls_index] == "W":
                filtered_contents[ls_index][inner_ls_index] = Water()
            
            elif filtered_contents[ls_index][inner_ls_index] == "F":
                filtered_contents[ls_index][inner_ls_index] = Fire()
            else:

                i = 0
                nums = ["1","2","3","4","5","6","7","8","9"]
                while i < len(nums):
                    if filtered_contents[ls_index][inner_ls_index] in nums:
                        filtered_contents[ls_index][inner_ls_index] = Teleport(filtered_contents[ls_index][inner_ls_index])
                        

                    i +=1

            inner_ls_index += 1

        ls_index += 1 
    
    
    return filtered_contents
    


