import time
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def kronometre():
    saniye = 0 #x
    dakika = 0 #y
    saat = 0 #z
    gun = 0 #t
    while True:
        if saniye == 60:
            dakika += 1
            saniye = 0
        if dakika == 60:
            saat += 1
            dakika = 0
        if saat == 24:
            gun +=1
            saat = 0

        if int(gun) <10:
            gunyazi = "0"+str(gun)
        else:
            gunyazi = str(gun)
        if int(saat) <10:
            saatyazi = "0"+str(saat)
        else:
            saatyazi = str(saat)
        if int(dakika) <10:
            dakikayazi = "0"+str(dakika)
        else:
            dakikayazi = str(dakika)
        if int(saniye) <10:
            saniyeyazi = "0"+str(saniye)
        else:
            saniyeyazi = str(saniye)


        cls()
        print(gunyazi,":",saatyazi,":",dakikayazi,":",saniyeyazi)
        saniye +=1
        time.sleep(1)

kronometre()
