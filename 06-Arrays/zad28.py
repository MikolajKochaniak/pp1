#med([1,1,2,2,100]) = 2
 

#med([1,1,2,6,100,200]) == (2+6)/2  = 4
def median(array):
    if len(array)%2==1:
        return array[len(array)//2]
    else:
        return (array[(len(array)//2)-1] + array[len(array)//2])/2

print(median([1]))