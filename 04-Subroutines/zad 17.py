def check_number_of_letter_occurences(letter, text):
    result = 0
    for l in text:
        if l == letter:
            result+=1
            
    return result 

print(check_number_of_letter_occurences("e","You never get a second chance to make a first impression"))
