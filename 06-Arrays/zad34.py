arr1=[1,2,3,4,5,]
arr2=[3,2,1,4,5,6,7]


is_subset = True

for x in arr1:
    x_exist_in_arr2 = False
    for y in arr2:
        if x==y:
            x_exist_in_arr2 = True
            break
    if not x_exist_in_arr2:
        is_subset = False
        break

print(is_subset)   
        

