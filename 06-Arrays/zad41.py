arr = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(arr)
j = arr[0]
arr[0]=arr[-1]
arr[-1]=j
print(arr)

