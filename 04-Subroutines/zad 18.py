def numberDigits(n):
    numer_str = str(n) 
    sum = 0

    for digit_str in numer_str:
        digit = int(digit_str)
        sum += digit

    return sum

print(numberDigits(7182))