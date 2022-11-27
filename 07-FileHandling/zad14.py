file_name = input("POdaj nazwę pliku: ")
with open(file_name) as f:
    sum = 0
    for line in f:
        sum+=1
    print(sum)