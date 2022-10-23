x = int(input("Podaj wartość dla x:  "))
y = int(input("Podaj wartość dla y:  "))
if x>0 and y>0:
    print(f'Punkt P({x},{y}) leży w pierwszej ćwiartce układu')
elif x<0 and y>0:
    print(f'Punkt P({x},{y}) leży w drugiej ćwiartce układu')
elif x<0 and y<0:
    print(f'Punkt P({x},{y}) leży w trzeciej ćwiartce układu')
elif x>0 and y<0:
    print(f'Punkt P({x},{y}) leży w czwartej ćwiartce układu')
elif x==0 and y==0:
     print(f'Punkt P({x},{y} leży w środku układu współrzędnych')    
elif x==0:
    print(f'Punkt P({x}, {y}) leży na osi y')
elif y==0:
    print(f'Punkt P({x}, {y}) leży na osi x') 