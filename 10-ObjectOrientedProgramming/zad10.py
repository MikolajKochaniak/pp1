class tv():
    def __init__(self):
        self.is_on = False
        self.channel = 1

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f'Tv jest włączony, Numer kanalu: {self.channel}')
        else:
            print("Tv jest wyłączony")
    def set_channel(self,channel):
        self.channel = channel

tvt = tv()
tvt.show_status()
tvt.turn_on()
tvt.set_channel(10)
tvt.show_status()
tvt.turn_off()
tvt.show_status()