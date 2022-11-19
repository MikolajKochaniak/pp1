arr = ["January","February","March","April","May","June", "July","August","September","October","November","December"]
def month(n):
    return arr[n-1]


for monthNumver in [1,2,11,12]:
    print(month(monthNumver))    