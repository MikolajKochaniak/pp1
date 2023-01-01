class Tv():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
        self._volume = 0

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            if self.channel<=len(self.channels):
                print(f'Tv jest włączony, Numer kanalu: {self.channel}:{self.channels[self.channel-1]}, volume : {self._volume}')
            else:
                print(f'Tv jest włączony, Numer kanalu: {self.channel}, volume : {self._volume}')
        else:
            print("Tv jest wyłączony")
    def set_channel(self,channel):
        if channel >= 1:
            self.channel = channel  
    def set_channels(self, channels):
        self.channels = channels
    def show_channels(self):
        print(self.channels)
    def increase_vol(self):
       if self._volume!=10:
            self._volume+=1 
    def decrease_vol(self):
        if self._volume!=0:
            self._volume-=1              