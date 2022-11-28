arr = [

{"population" :"22 mil"},
{"num" :"+56"},
{"turist":"many"},
{"popularity":"Large"},
{"sports":"football","123":"123"}

]
i = 0
while i<=len(arr):
    for k,v in arr[i].items():
        print(v, end="  ")
        i+=1