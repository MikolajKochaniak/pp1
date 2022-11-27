with open("15.txt") as f:
    num_of_line=0
    for line in f:
        num_of_line+=1
        if num_of_line%5==0:
            input()
            print(line)
        else:
            print(line)

# with open("15.txt") as f:

#     while True:
#         line = ''
#         for i in range(0,5):
#           line = f.readline()
#           if line  == '':
#             break
#           else:
#             print(line)
#         if line == '' :
#             break   
#         input()           


