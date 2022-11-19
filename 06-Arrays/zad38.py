#x = liczba rzędów y = liczba kolumn

#[]

#[[]]

# [[0,0,0], [0,0,0]]

def create_2d_arr(x,y):
    new_arr: list[list[int]] = []
    for i in range(0,x):
        new_arr.append([])
        for j in range(0,y):
            new_arr[i].append(0)   
    return new_arr

#print(create_2d_arr(3,5))

