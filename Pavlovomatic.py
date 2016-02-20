import winsound
import time

def getPosition():
    return 1

def getTreat():
    print("Good Job!")

winsound.PlaySound('artza1.wav', winsound.SND_FILENAME)
time.sleep(10)

ipAns = 1
inPlace = False
position = 0

while not inPlace:
    position = getPosition()
    if position == 1:
        inPlace = True;
    else:
        winsound.PlaySound('artza1.wav', winsound.SND_FILENAME)
        time.sleep(10)

sit = True
for x in range(0,5):
    if sit:
        winsound.PlaySound('shev1.wav', winsound.SND_FILENAME)
        time.sleep(5)
        position = getPosition()
        if position == 2:
            getTreat()
            sit = False
    else:
        winsound.PlaySound('artza1.wav', winsound.SND_FILENAME)
        time.sleep(5)
        position = getPosition()
        if position == 1:
            getTreat()
            sit = True



