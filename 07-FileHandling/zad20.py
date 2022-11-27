import random
with open("20.txt","w") as f:
    for i in range(50):
        random_num = random.randint(100,999)
        random_str = str(random_num) + "\n"
        f.write(random_str)