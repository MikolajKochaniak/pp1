import re
with open("grades.txt") as grades:
    grades_content = grades.read()
    final_grades = re.findall("[+-]?[0-9]+\.[0-9]+",grades_content) 
    sum = 0
    for i in final_grades:
        i_flo = float(i) 
        sum +=i_flo
print(sum/len(final_grades))
