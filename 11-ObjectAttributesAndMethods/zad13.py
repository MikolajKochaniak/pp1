import math
class Calculator():
    @staticmethod
    def circle(r):
        area = math.pi*r**2
        return area
    def triangle(a,h):
        area = a*h/2
        return area
    def rectangle(a,b):
        area = a*b
        return area

print(Calculator.circle(10))
print(Calculator.triangle(5,3))
print(Calculator.rectangle(5,3))
