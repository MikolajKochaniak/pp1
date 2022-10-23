# for x in range(1,10):
#     if x<6:
#         print("*"*x)
#     else:
#         print("*"*(10-x))


stars_str = "*"
for x in range(1,10):
    print(stars_str)
    if x<5:
        stars_str = stars_str + "*"
    else:
        stars_str = stars_str[:-1]      


