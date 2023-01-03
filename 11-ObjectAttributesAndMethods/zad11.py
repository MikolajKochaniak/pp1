class Phone():
    def __init__(self,colour,model):
        self.is_on = False
        self.colour = colour
        self.model = model
    def turn_on(self):
        if self.is_on == False:
            self.is_on = True
    def turn_off(self):
        if self.is_on == True:
            self.is_on == False
    def __str__(self):
        return f'Colour is {self.colour}, model is {self.model}, is the phone on-- {self.is_on}'

tele = Phone("black","iphone 14")
tele.turn_on()
print(tele)


