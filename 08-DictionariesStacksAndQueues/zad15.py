dictionary = {
        'A':'Alpha', 
        'B':'Bravo',
        'C':'Charlie', 
        'D':'Delta', 
        'E':'Echo', 
        'F':'Foxtrot', 
        'G':'Golf', 
        'I':'India', 
        'J':'Juliet', 
        'K':'Kilo', 
        'L':'Lima', 
        'M':'Mike', 
        'N':'November', 
        'O':'Oscar', 
        'P':'Papa', 
        'Q':'Quebec', 
        'R':'Romeo', 
        'S':'Sierra', 
        'T':'Tango', 
        'U':'Uniform', 
        'V':'Victor', 
        'W':'Whiskey', 
        'X':'Xray', 
        'Y':'Yankee', 
        'Z':'Zulu'
}

file = open("ICAO.txt", "w")

for k,v in dictionary.items():
    string = k + " " + v + "\n"
    file.write(string)