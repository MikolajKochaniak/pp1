with open("21.txt","w") as f:
    for i in range(1,11):
        i2 = i**2
        i3 = i**3
        i2_str = str(i2) + ","
        i3_str = str(i3) + "\n"
        str_i = str(i)+ ","
        f.write(str_i + i2_str + i3_str)
        # f.write(f"{i}, {i**2}, {i**3} \n")
