# [5,1,9,6,1]

# 1.
#[1,1,5,6,9,9, 9 ,9 ]
# [1,5,6,9]
# arr[:-2]

# list(set(arr.sort())_[:-2]
# 1. sort asc, do a set and take index len - 2


# 2.
# Find max, remove max  arr.remove(max) from array, find max

# 3. create two variables max, secondMax and loop with for
arr = [5,1,9,6,1]
max = arr[0]
secondMax = max
for i in range(0,len(arr)):
    if arr[i]>max:
        secondMax = max
        max = arr[i]
    if arr[i]>secondMax and arr[i] < max:
        secondMax = arr[i]   
    else:
        continue
print(secondMax)
        
