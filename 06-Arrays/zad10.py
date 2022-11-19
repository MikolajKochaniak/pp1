arr = [4,2,5,6,7,8,4,3,2,1]

i = 0
even = 0
odd = 0
while i < len(arr):
    i+=1
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1

print(even,odd)
