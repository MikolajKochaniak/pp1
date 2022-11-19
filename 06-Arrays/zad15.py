arr = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(arr)):
    row = arr[i]
    for j in range(0,len(row)):
        if i==j:
            arr[i][j]+=1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()