import numpy as np

from calculatearea import AreaEstimator
from math import sqrt

area_estimator = AreaEstimator(filename='rancho_rd.jpg',  # name of the image in the directory
                               color_range=((0, 0, 118), (100, 100, 255)),
                               default_area_color=(255, 20, 160))  # BGR purple

A_px = area_estimator.get_area(return_pixels=True)
ft_per_pixel = sqrt(131193.8 / A_px)  # plot size - 30.56 acres, img size - 447x588 px
print(ft_per_pixel)

area_estimator.show_images()

# with tighter restraints
area_estimator.color_lower_limit = np.array([0, 0, 130], np.uint8)
area_estimator.color_upper_limit = np.array([50, 50, 255], np.uint8)
area_estimator.area_color = (100, 200, 200)

A_px = area_estimator.get_area()
area_estimator.show_images()

ft_per_pixel = sqrt(131193.8 / A_px)
print(ft_per_pixel)
