arr = [[-38, 19], [5,40],[-7,11],[29,16]]
max = arr[0][0]
min = arr[0][0]
i_max = 0
j_max = 0
i_min = 0
j_min = 0
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if arr[i][j]>max:
            max = arr[i][j]
            i_max = i
            j_max = j
        if arr[i][j]<min:
            min = arr[i][j]
            i_min = i
            j_min = j
            
print(max,min,i_max,j_max,i_min,j_min)

