# [1,2,3,4] vs [1,2,3,5]
def compare(array1,array2):
    if len(array1) != len(array2):
        return False
    for i in range(0,len(array1)):
        if array1[i] == array2[i]:
            continue
        else: 
            return False
    return True
        
print(compare([5,3,1],[5,8,1]))  