__author__ = "Hunter Boyd"
__email__ = "hjboyd@email.sc.edu"
__version__ = 1.0

"""
main.py is the implementation of my submission for CSCI 550 project 1.
All of the methods used to calculate the area, along with explanations, are in calculatearea.py.
Both calculatearea.py and PartyRockFire.jpeg must be in the same directory as this file.
This file provides a brief overview of the functions I created in AreaEstimator in order to estimate and
visualize the area of contiguous, semi-polygonal shapes.

This project depends on numpy and opencv-python, which can be installed via pip.
A README has been included with some basic setup instructions.
A backup_script.py has been included in case it must be run as a single file, although it lacks visual features.
"""

from calculatearea import AreaEstimator

if __name__ == "__main__":

    # First we create an instance of AreaEstimator
    area_estimator = AreaEstimator()
    # The class has default values; this is equivalent to:
    # area_estimator = AreaEstimator(filename='PartyRockFire.jpeg',  # name of the image in the directory
    #                                feet_per_pixel=8188/215,  # the conversion ration from pixels to feet
    #                                color_range=((0, 0, 118), (100, 100, 255)),  # dark to light red BGR tuples
    #                                area_color=(147, 20, 255))  # BGR pink

    # Now we calculate the area in square feet, then print the value rounded to 3 significant figures
    A = area_estimator.get_area()
    # You can also get the area in pixels
    A_px = area_estimator.get_area(return_pixels=True)
    print(f'\nThe area of the Party Rock Fire is approximately {round(A, -6)} square feet (or {A_px} pixels)')

    # display the images
    area_estimator.show_images()
