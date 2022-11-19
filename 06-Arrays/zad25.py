def occurs(number,array):
    for i in range(0,len(array)):
        if number == array[i]:
            return True
        else:
            continue
    return False
    

print(occurs(239,[0,8,23]))