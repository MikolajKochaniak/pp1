import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperatures = re.findall("\d{2}",message)
sum = 0
for temp_str in temperatures:
    temp = int(temp_str)
    sum += temp
print(sum/len(temperatures))


