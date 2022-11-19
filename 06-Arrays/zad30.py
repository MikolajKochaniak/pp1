def minmax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(0,len(arr)):
        if arr[i]> max:
            max = arr[i]
        if arr[i]<min:
            min = arr[i]
    return [min,max]



print(minmax([4,2,8,4,7,9,5]))
