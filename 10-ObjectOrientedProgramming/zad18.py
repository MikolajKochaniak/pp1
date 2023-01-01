class calculator():
    def __init__(self,arr):
        self.arr = arr
    def diplay(self):
        for i in self.arr:
            print(self.arr,end=" ")
    def inc(self,no):
        self.arr.append(no)
    def min(self):
        self.min = min(self.arr)
    def max(self):
        self.max = max(self.arr)
    def mean(self):
        self.mean = sum(self.arr)/len(self.arr)
    def status(self):
        print(f'min is {self.min}, max is {self.max}, mean is {self.mean}')
    def status2(self):
        print(self.arr)

calcu = calculator([12,37,6,9,17])
calcu.inc(14)
calcu.status2()
calcu.max()
calcu.min()
calcu.mean()
calcu.status()


    
    
        