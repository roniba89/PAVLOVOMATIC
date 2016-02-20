import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


def load_sit_images(folder):
    current = None
    index = 0;
    iterations = 1
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)

        if img is not None:
            index += 1
            if iterations == 343:
                break
            if index % 2 == 0:
                img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
                if current is None:
                    current = img
                else:
                    iterations += 1
                    current = np.concatenate((current, img), axis=1)
    return current


def load_ground_images(folder):
    current = None
    index = 0
    iterations = 1
    for filename in os.listdir(folder):
        if iterations > 342:
            break
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)

        if img is not None:
            index += 1
            if index % 3 == 0:
                img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
                if current is None:
                    current = img
                else:
                    iterations += 1
                    current = np.concatenate((current, img), axis=1)
    print "ground"
    print iterations
    return current


def load_empty_images(folder):
    current = None
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)

        if img is not None:
            img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
            if current is None:
                current = img
            else:
                current = np.concatenate((current, img), axis=1)
    return current


def correlate_image(img, allStateImages, methods):
    for meth in methods:
        print ("calculating " + meth)
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img, allStateImages, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print "min val " + str(min_val) + " max val " + str(max_val) + " min_loc " + str(min_loc) + " max_loc " + str(
            max_loc)
        return max_loc[1] < 200


#
# print ("loading sit row")
# sitRow = load_sit_images("C:\\Pavlovomatic\\data\\pavlovomatic\\images\\sit")
# print ("loading ground row")
# groundRow = load_ground_images("C:\\Pavlovomatic\\data\\pavlovomatic\\images\\ground")
# print ("loading empty row")
# emptyRow = load_empty_images("C:\\Pavlovomatic\\data\\pavlovomatic\\images\\empty")
# print ("vertical concatination")
# allStateImages = np.concatenate((np.concatenate((sitRow, groundRow), axis=0), emptyRow), axis=0)
allStateImages = cv2.imread("all_states.png", cv2.IMREAD_GRAYSCALE)

# sitAndEmptyStateImages = np.concatenate((sitRow, emptyRow), axis=0)
img = cv2.imread("C:\\Users\\ishai\\PycharmProjects\\Pavlovomatic\\gadi1455965615.95.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
# # just correlation
methods = ['cv2.TM_CCORR_NORMED']
#
# # All the 6 methods for comparison in a list
# methods = ['cv2.ADAPTIVE_THRESH_GAUSSIAN_C', 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
print correlate_image(img, allStateImages, methods)

print "\nreal data"
img = cv2.imread("C:\\Users\\ishai\\PycharmProjects\\Pavlovomatic\\gadi1455965649.4.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
print correlate_image(img, allStateImages, methods)

print "\nimage from data"
img = cv2.imread("C:\\Pavlovomatic\\data\\pavlovomatic\\images\\empty\\sit00014.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
print correlate_image(img, allStateImages, methods)


def is_in_frame(image):
    allStateImages = cv2.imread("all_states.png", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
    methods = ['cv2.TM_CCORR_NORMED']
    return correlate_image(image, allStateImages, methods)


