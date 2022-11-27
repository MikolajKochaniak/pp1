with open("15.txt") as input_file:
    with open("17_copy.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)
