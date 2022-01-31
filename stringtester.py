# k = 0
# string = "**A31"
# while k < len(string):


#     valid_letters = ["A"," ","X","Y","*","1","2","3","4","5","6","7","8","9","W","F"]
#     if string[k] not in valid_letters:
#         raise ValueError("Bad letter in configuration file: {}".format(string[k]))
    
#     k += 1

# lines = ['**X**', '*   *', '**Y**']
# i = 0 
# while i < len(lines):
#     string = lines[i]
#     k = 0
#     while k < len(string):

#         valid_letters = ["A"," ","X","Y","*","1","2","3","4","5","6","7","8","9","W","F"]
#         if string[k] not in valid_letters:
#             raise  ValueError("Bad letter in configuration file: {}".format(string[k]))
#         # occurence_x = "X"
#         # occurence_y = "Y"
#         k += 1
    
#     i+=1

# st = "hi"
# x_count = 0
# x_count += st.count("X")
# print(x_count)
ls = ['2', '3', '2', '4', '4','5']
counts = [[x,ls.count(x)] for x in set(ls)]
print(counts)
print(counts[0][1])
x = 0
while x < len(counts):
    if counts[x][1] != 2:
        print("this number does not have matching pair {}".format(counts[x][0]))
        break
    x += 1