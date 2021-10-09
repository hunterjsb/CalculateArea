#!/usr/bin/env python
import numpy as np
import cv2 as cv
"""
|-------------------------------------------------------------|
| BACKUP FILE FOR USING THIS PROJECT AS A SINGLE SCRIPT       |
| THE MAIN PROJECT IS RUN BY main.py                          |
| THIS FILE DOES NOT DEPEND ON ANY OTHER FILES THAN THE IMAGE |
|-------------------------------------------------------------|
"""

FEET_PER_PX = 8188 / 215  # ratio from the image scale

# open the image
prf = cv.imread('PartyRockFire.jpeg', 1)

if __name__ == "__main__":

    # set range for "red"
    redlo = np.array([0, 0, 118], np.uint8)
    redhi = np.array([100, 100, 255], np.uint8)

    # get red pixels
    red = cv.inRange(prf, redlo, redhi)

    # get indices of red cells then max and min
    indices = np.where(red > 0)
    col_max, col_min = max(indices[1]), min(indices[1])
    rows_with_red = np.unique(indices[0], return_counts=True)

    # basic data verification using a few test cases
    # for i in [(10, 55), (5761, 356), (8988, 525), (9078, 527), (9517, 555)]:
    #     print(f"index {i[0]} valid? ", indices[0][i[0]] == i[1])
    # print(indices[1][len(indices[1])-1])

    # now find the max horizontal distance between the white pixels on each row
    i = 0
    distances = []
    for count in rows_with_red[1]:
        distance = indices[1][i:i+count][-1] - indices[1][i:i+count][0]  # indices[1] is sorted
        distances.append(distance + 1)
        i += count

    # print the results
    print("the area is ", sum(distances), " pixels")
    print("which is ", round(sum(distances)*FEET_PER_PX*FEET_PER_PX, 2), " sq feet")
