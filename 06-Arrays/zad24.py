arr = [2,3,2,5,8,1,9,8]
# for i in range(0,len(arr)):
#     occurs_at_least_one_more = False
#     for j in range(0,len(arr)):
#         if i == j:
#             continue
#         else:
#             if arr[i] == arr[j]:
#                 occurs_at_least_one_more=True
#                 break
#     is_unique = not occurs_at_least_one_more     

#     if is_unique:
#         print(arr[i])


# x = count(2, arr)

def count(el, arr):
    sum = 0
    # for x in arr:
    #     if x == el:
    #         sum+=1
    for i in range(0,len(arr)):
        if arr[i]==el:
            sum+=1
    return sum

# arr= [2,3,2,5,8,1,9,8]

# x = is_unique(2, arr)
def is_unque(el, arr):
    if count(el, arr) == 1:
        return True
    else: 
        return False

for i in range(0,len(arr)):
    if is_unque(arr[i], arr) == True:
        print(arr[i])







