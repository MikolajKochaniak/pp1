arr = [[True,False],[True,True],[False,False]]


# [[False,True],[False,False],[True,True]]


# test = [False, True, 10]

# enumerate(test)

# for i, val in [(0, False), (1, True), [2,10]]:

for i in range(0,len(arr)):
    row = arr[i]
    for j in range(0,len(row)):
        arr[i][j] = not arr[i][j]


# for i, row in enumerate(arr):
#     for j, value in enumerate(row):
#         arr[i][j] = not value


print(arr)



