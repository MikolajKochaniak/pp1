N = int(input("Podaj liczbę, dla której chcesz sprawdzić czy jest liczbą pierwszą"))
if N>1:
    flag = True
else:
    flag = False
    
for i in range(2,int(N/2 + 1)):
    if N%1==0:
        flag = False
        break

if flag == True:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")


