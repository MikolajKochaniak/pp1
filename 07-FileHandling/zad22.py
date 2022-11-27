import csv
with open("students.txt") as f:
    csv_reader = csv.reader(f)
    csv_list = []
    for row in csv_reader:
        csv_list.append(row)
    csv_list.pop(0)
    print(csv_list) 
    for i in range(0,len(csv_list)):
        int_age = int(csv_list[i][2])
        if int_age>=30:
            print(f"{csv_list[i][0]} {csv_list[i][1]} {csv_list[i][4]} ")


