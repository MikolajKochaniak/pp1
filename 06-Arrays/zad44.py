from zad38 import create_2d_arr

def transpose_matrix(m):

    a = len(m)
    b = len(m[0])
    result = create_2d_arr(b,a)


    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            result[j][i]=m[i][j]
    return result        


m=[[1,2,3],[4,5,6],[7,8,9]]

print(m)
print(transpose_matrix(m))