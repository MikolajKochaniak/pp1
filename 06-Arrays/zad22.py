arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]

def exists_in_arr(el, arr):
    for x in arr:
        if el == x:
            return True
    return False 

# for value_form_arr1 in arr1:
#     should_be_displayed = True
#     for value_form_arr2 in arr2:
#         if value_form_arr1 == value_form_arr2:
#             should_be_displayed = False
#             break
#     if should_be_displayed:
#         print(value_form_arr1)    


for value_form_arr1 in arr1:
    if not exists_in_arr(value_form_arr1, arr2):
        print(value_form_arr1)  
