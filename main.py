__author__ = "Hunter Boyd"
__email__ = "hunterjsb@gmail.com"
__version__ = 1.0
__date__ = "10/10/2021"

"""
main.py is the implementation of my submission for CSCI 550 project 1.
All of the methods used to calculate the area, along with explanations, are in calculatearea.py.
Both calculatearea.py and PartyRockFire.jpeg must be in the same directory as this file.
This file provides a brief overview of the functions I created in AreaEstimator in order to estimate and
visualize the area of contiguous, non-branching shapes.

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
    #                                default_area_color=(147, 20, 255))  # BGR pink

    # Now we calculate the area in square feet, then print the value rounded to 3 significant figures
    A = area_estimator.get_area()

    # You can also get the area in pixels
    A_px = area_estimator.get_area(return_pixels=True)
    print(f'\nThe area of the Party Rock Fire is approximately {round(A, -6)} square feet (or {A_px} pixels)')

    # display the two images, then press any key to continue
    area_estimator.show_images()

    # you can can also get the area by adding over the columns instead of rows
    A_px_by_col = area_estimator.get_area(return_pixels=True, by_columns=True, fill_color=(255, 20, 147))  # Blue?
    A_by_col = A_px_by_col*area_estimator.px_size
    print(f'\nThe area as estimated by column-sum: {round(A_by_col, -6)} square feet ({A_px_by_col} px)')
    area_estimator.show_images()

    # and finally we can see the difference between the areas by not clearing the selected image
    area_estimator.get_area()  # horizontal sum
    area_estimator.area_color = (51, 244, 244)  # yellow
    area_estimator.get_area(by_columns=True)  # vertical sum
    area_estimator.show_images()

    print(f'\nthe average of the two methods is: {round(((A + A_by_col) / 2), -6)} square feet')
