import array as arr 
import random
arr1 = arr.array('i',[3,7,1,0,4])
print(arr1)
#arr2 = arr.array([[2,3],[7,1],[0,4]]) - nie działa
#print(arr2)
arr3 = arr.array('i',[7 for i in range(5)])
arr4 = arr.array('i',[i for i in range(1,10)])
arr5 = arr.array('i',[i*2 for i in range(1,10)])
arr6 = arr.array('i',[random.randint(1,20) for i in range(10)])
arr7 = arr.array('i',[[] for i in range(5)])
arr8 = arr.array('i',[[1 for i in range(2)] for j in range(4)] )
arr9 = arr.array('i', [[random.randint(1,20) for i in range(3)] for j in range(5)])
arr10 = arr.array('i'[4,0,3])
arr11 = arr.array('i'[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
arr12 = arr.array('i'[1,2,3,4,5,6,7,8,9,10.11,12,13,14,15.16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
arr13 = arr.array('i'[0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0])

