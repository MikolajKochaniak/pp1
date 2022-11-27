with open("15.txt") as input_file:
    content = input_file.read()
    with open("15_copy.txt", "w") as output_file:
        output_file.write(content)