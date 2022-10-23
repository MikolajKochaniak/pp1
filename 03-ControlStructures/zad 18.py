cash_amount = int(input(" Enter the amount in PLN: "))

five_amount = 0
two_amount = 0
one_amount = 0


to_be_balanced = cash_amount

while to_be_balanced > 0:
    if to_be_balanced >= 5: 
        to_be_balanced -= 5
        five_amount += 1
    elif to_be_balanced >=2:
        to_be_balanced -= 2
        two_amount += 1    
    else:
        to_be_balanced -= 1
        one_amount += 1 

print(f'Fives: {five_amount}, twos: {two_amount}, ones: {one_amount}')

 



# cash_amount = 5*five_amout + 2 * two_amount + 1* one_amount