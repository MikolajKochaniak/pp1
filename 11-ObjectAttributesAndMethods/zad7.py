class Student():
    university = "UEK Kraków"
    id = 100000
    def __init__(self,name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Student.id
        self.id +=1
    
    def __str__(self):
        return f'Name: {self.name}\nSurname:{self.surname}\nUniversity: {Student.university}\nField: {self.field}\nId: {self.id}'

student = Student("Mikołaj","Kochaniak","Informatyka Stosowana")
print(student)




