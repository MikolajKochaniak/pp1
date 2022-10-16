import random
computer_result = random.randint(1,6)
player_guess = input("Co wylosowała kostka?")


if computer_result == player_guess:
    print("true")
else:
    print("false")    


  


