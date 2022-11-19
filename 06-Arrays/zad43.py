# [[1 , 0 ,0],
# [0, 1, 0],
# [0, 0, 1]]

# []
# [[],[],[],[] x i]
def identity_matrix(n):
    list =[]
    for i in range(0,n):
        list.append([])
        for j in range(0,n):
            list[i].append(0)
            if i == j :
                list[i][j] = 1
    return list


print(identity_matrix(3),end = " ")