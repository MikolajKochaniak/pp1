import random
class Thermometer():
    def __init__(self):
        self.temp = 0
        self.is_on = False
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def temp_display(self):
        if self.temp < 37.0:
            print(f'{self.temp} is ok')
        elif self.temp>=37.0 and self.temp<41.0:
            print(f'{self.temp} is fever')
        else:
            print(f'{self.temp} CRITICAL TEMPERATURE')
    def temp_measure(self):
        self.temp = random.uniform(34.0,42.0)
    def status(self):
        print(f'Thermometer is on : {self.is_on}')  

    

