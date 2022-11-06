# x**n = x**1 * x**(n-1)
# x**n = x**(n-1+1)
# x**n = x**n

# x**n = x * x**(n-1)


# power(5,3) = 5 * power(5,2)
# return  5 * power(5,2)
# 
# 
#  
# power(5,2) = 5 * power(5,1)
# power(5,1) = 5 * power(5,0) 
# power(5,0) = 5 * power(5,-1)
# power(5,-1) = 5 * opo


# power(x,0) = 1

def power(x,n):

    if n == 0:
        return 1
    else:
        return x*power(x,n-1)

            

print(power(5,3))
