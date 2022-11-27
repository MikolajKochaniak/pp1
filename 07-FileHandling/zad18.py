with open("MeatAndFish.txt") as f1:
    with open("GrainsAndBread.txt") as f2:
        content = f1.read()+f2.read()
with open("shoppinglist.txt", "w") as output_file:
    output_file.write(content)