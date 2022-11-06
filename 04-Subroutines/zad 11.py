def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

# 5! = 1 * 2 * 3 * 4 * 5
# 5! = 4! * 5
# 4! = 3! * 4


    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
  
x = 5
print( f"{x}! = {factorial(x)}" )
