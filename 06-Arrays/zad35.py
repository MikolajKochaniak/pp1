import random
def rand_elem(array):
    random_index = random.randint(0,len(array)-1)
    random_num = array[random_index]
    return random_num
    

print(rand_elem([1,2,3,4,5,6,7,8]))