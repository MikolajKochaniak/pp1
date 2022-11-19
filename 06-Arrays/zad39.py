arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


# 6 = 3*2 = (2+1)*(1+1)

for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        arr[i][j]= (j+1)*(i+1)
        print(f'{arr[i][j]:2}', end=" ")
    print()    
