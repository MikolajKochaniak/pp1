def trans(arr):
    new_arr=""
    for i in range(0,len(arr)):
        arr[i]= str(arr[i])
        new_arr+=arr[i]
        new_arr+=","
    return new_arr

print(trans([5,4,3,2,6,5]))