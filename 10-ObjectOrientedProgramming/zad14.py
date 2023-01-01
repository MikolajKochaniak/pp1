from Tv import Tv

tv = Tv()
tv.turn_on()
tv.show_status()

tv.increase_vol()
tv.increase_vol()
tv.increase_vol()
tv.show_status()

for i in range(0,100):
    tv.increase_vol()
tv.show_status()    


for i in range(0,100):
    tv.decrease_vol()
tv.show_status()  

tv.show_status()  