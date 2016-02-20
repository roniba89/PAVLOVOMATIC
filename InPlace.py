import winsound
import time
import state_resolver
import cv2
import serial





state_resolver.is_in_frame(
    cv2.imread("C:\\Pavlovomatic\\data\\pavlovomatic\\images\\empty\\sit00014.png", cv2.IMREAD_GRAYSCALE))
from __builtin__ import xrange


def getImage(camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


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
    # file = "C:\Users\ronib\Desktop\test_image.png"
    # cv2.imwrite(file, cameraCapture)
    # cv2.imshow('image',cameraCapture)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    ipAns = state_resolver.is_in_frame(cameraCapture)

    del (camera)
    # return True
    return ipAns


def getTreat():
    #print("Good Job!")
    ser = serial.Serial('COM3', 9600, timeout=0)
    #var = raw_input("Enter 0 or 1 to control led: ")
    ser.write(1)


def isInPosition(position):
    ipAns = getPosition()
    if position == ipAns:
        getTreat()
    else:
        goToPosition(position)


def goToPosition(position):
    if position:
        winsound.PlaySound('artza1.wav', winsound.SND_FILENAME)
        time.sleep(6)
        isInPosition(position)
    else:
        winsound.PlaySound('shev1.wav', winsound.SND_FILENAME)
        time.sleep(6)
        isInPosition(position)


loopIndex = 0;
while loopIndex < 4:
    goToPosition(True)
    goToPosition(False)
    goToPosition(True)
    goToPosition(False)
