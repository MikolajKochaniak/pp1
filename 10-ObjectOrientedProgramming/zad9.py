class Tv():
    def __init__(self):
        print("Creating new TV")
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print("Tv jest włączony")
        else:
            print("Tv jest wyłączony")

tvt = Tv()
tvt.show_status()
tvt.turn_on()
tvt.show_status()
tvt.turn_off()
tvt.show_status()



