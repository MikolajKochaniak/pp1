def sum(N):
    if N==1:
        return 1
    else:
        return sum(N-1) + N

result = sum(10)    
print(result) 

print((lambda x : x+1)(10))



# Warunek brzegorwy / warunek stopu
    # sum(1) = 1

    # sum(4) = 1 + 2 + 3 + 4 
    # sum(5) = 1 + 2 + 3 + 4 + 5
    # sum(5) = sum(4) + 5


    #Ogólny przepis
    # sum(N) = sum(N-1) + N
