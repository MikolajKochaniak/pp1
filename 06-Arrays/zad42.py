arr = [[1, 0, 0, 0, 10], [2, 0, 0, 0, 20], [3, 0, 0, 0, 30]]
print(arr)
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if j ==0:
            x = arr[i][-1]
            arr[i][-1]= arr[i][j]
            arr[i][j] = x

print(arr)

