import winsound
import time
import cv2
from __builtin__ import xrange

def getImage(camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im

def getPosition():
    cameraPort = 0
    rampFrames = 30
    camera = cv2.VideoCapture(cameraPort)
    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in xrange(rampFrames):
        temp = getImage(camera)
    print("Taking image...")
    cameraCapture = getImage(camera)
    #cv2.imshow('image',cameraCapture)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #ipAns = getState(cameraCapture)
    del(camera)
    return 1
    #return ipAns

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