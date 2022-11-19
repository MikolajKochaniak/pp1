arr = [[1, 0, 0, 0, 10], [2, 0, 0, 0, 20], [3, 0, 0, 0, 30]]
print(arr)
for i in range(0,len(arr)):
    x = arr[i][-1]
    arr[i][-1] = arr[i][0]
    arr[i][0] = x

print(arr)

