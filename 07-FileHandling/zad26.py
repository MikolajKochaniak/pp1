import re
with open("26.txt") as text:
    text_content = text.read()
    words = re.findall("\w{6}",text_content)
    for i in words:
        print(i)
        

   