arr = [15, 8, 31, 47, 2, 19]
for i in range(0,len(arr)//2):
    #if i < len(arr)//2:
        rev_i = len(arr)-1-i
        #! temporary value to swap to list elements
        temp = arr[i]
        arr[i] = arr[rev_i]
        arr[rev_i] = temp
print(arr)    