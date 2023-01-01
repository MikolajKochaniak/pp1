from Tv import Tv

tv = Tv()

tv.show_status()
tv.turn_on()
tv.show_channels()
tv.show_status()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv.show_channels()
tv.show_status()
tv.turn_off()