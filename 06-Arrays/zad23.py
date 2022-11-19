# a1 = [8,4,3]

# swap(0,2, a1)

#[3,4,8]

# 3 <0,3) {0,1,2}

# 

def swap(i, j, arr):
    first_value = arr[i]
    second_value = arr[j]
    
    arr[j] = first_value
    arr[i] = second_value
    

def bubblesort(array):

    while True: #zawsze do nieskonczoności
        was_swapped = False
        for i in range(0,len(array)-1):
            if array[i]>array[i+1]:
                swap(i, i+1, array)
                was_swapped = True
        if was_swapped==False:
            break        

test_arr = [7,2,3,6]

# [7,2,3,6]

# [2,7,3,6]

# [2,3,7,6]

# [2,3,6,7]


print(test_arr)
bubblesort(test_arr)
print(test_arr)