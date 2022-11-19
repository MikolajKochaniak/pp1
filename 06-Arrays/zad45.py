arr = [[2,3],[1,5]]
def flatmap(arr):
    arr2 =[]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            arr2.append(arr[i][j])
    return arr2

print(flatmap(arr))

# (flatMap) [2,3,1,5]