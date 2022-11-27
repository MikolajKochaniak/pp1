import re
message = "To be, or not to be, that is the question"
words = re.findall("\w+",message)
num_of_words = len(words)
print(num_of_words)