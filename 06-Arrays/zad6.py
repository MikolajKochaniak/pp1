
arr1 = [2, 3, 7, 5, 4]
print(arr1)
sum = 0 
for i in arr1:
    sum+=1
print(sum)
#print(len(arr1))
print(arr1[0])
print(arr1[1])
print(arr1[-1])
print(arr1[0]+ arr1[len(arr1)-1])
print(arr1[int(len(arr1)/2)])
for j in range(0,len(arr1)):
    print(arr1[j], end=" ")
print()

for x in range(0, int(len(arr1)/2)):
    print(arr1[x], end=" ")