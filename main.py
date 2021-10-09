# main

import numpy as np
import cv2 as cv
import time
# OPENCV IS --- BLUE, GREEN, RED --- (BGR)
"""
the image is 860 x 679 pixels (679 rows x 860 columns)
need to loop through about ~600k pixels x 3 channels = ~1.8 million ints
"""

prf = cv.imread('PartyRockFire.jpeg', 1)


def display(img):
    """function to show the image"""
    cv.imshow('Party Rock Fire', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":

    # set range for "red"
    redlo = np.array([0, 0, 118], np.uint8)
    redhi = np.array([100, 100, 255], np.uint8)

    # get red pixels
    red = cv.inRange(prf, redlo, redhi)

    # loop
    print((np.where(red > 0)))

    # display(red[red >= 0])
