
Liczba = int(input("Enter number: "))
sum = 0 
quantity = 0

while Liczba != 0:
    sum += Liczba
    quantity +=1
    Liczba = int(input("Enter number: "))

mean = sum/quantity
print(f": Quantity= {quantity}, Sum={sum}, Mean={mean}")


