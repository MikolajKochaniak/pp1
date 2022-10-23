correct_password = "0805"
for x in range(0,3):
    password_attempt = input("Proszę o podanie hasła: ")
    if correct_password == password_attempt :
        print("Correct")
        break
    else:
        print("Incorrect...")
        if x==2:
            print("Sorry, your payment card has been blocked.")


        
