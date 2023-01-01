from Tv import Tv


tv = Tv()
tv.turn_on()
tv.set_channel(2)
tv.set_channels(["TVP1", "TVP2", "TV Trwam"])
tv.show_status()
tv.set_channel(3)
tv.show_status()
tv.set_channel(-100)
tv.show_status()

