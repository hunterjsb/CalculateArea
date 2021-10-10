import numpy as np
import cv2 as cv


class AreaEstimator:
    """
    A class that can estimate the area of contiguous shapes based on a colored outline.
    It also provides a visual representation of the estimated area.

    The main method for this class, get_area, calculates to area of a shape in the loaded image;
    it sums the differences between the min and max pixels over the given axis (rows by default).
    This find the area of each row, which has a height of 1, so it equal to its length.

    AreaEstimator has four inputs, all have a default for Project 1:

    Parameters:
    -----------
        :param filename: name and filepath of the image file to load
        :param feet_per_pixel: the ratio of feet to pixels
        :param color_range: the minimum and maximum BGR colors that will be picked up by cv.inRange
        :param default_area_color: the color used to fill in the estimated area - not related to calculation+
    """

    def __init__(self,
                 filename='PartyRockFire.jpeg',
                 feet_per_pixel=8188/215,
                 color_range=((0, 0, 118), (100, 100, 255)),
                 default_area_color=(147, 20, 255)):
        # open the file
        self.img = cv.imread(filename)

        # set color tolerance
        self.color_lower_limit = np.array(color_range[0], np.uint8)
        self.color_upper_limit = np.array(color_range[1], np.uint8)
        self.area_color = default_area_color  # for filling in estimated area

        # initialize empty array for selected pixels
        self._selected = np.zeros(self.img.shape, np.uint8)
        self.px_size = feet_per_pixel * feet_per_pixel

    def show_images(self, clear_selected=True) -> None:
        """function to show the image & exit when a key is pressed"""

        # display selected pixels if applicable
        if np.any(self._selected):
            cv.imshow('Selected Area', self._selected)

        # display the image
        cv.imshow('Party Rock Fire (Press Any Key...)', self.img)
        cv.waitKey(0)  # exit on any key

        # reset the selected pixels to black
        if clear_selected:
            self._selected = np.zeros(self.img.shape, np.uint8)

    def get_area(self, return_pixels=False, by_columns=False, fill_color=None) -> float:
        """function to estimate the area of a selected contiguous shape, default row-by-row"""

        # get an array of pixels that are within the range, value will be 255 or 0
        in_range = cv.inRange(self.img, self.color_lower_limit, self.color_upper_limit)
        if by_columns:  # rotate the image 90 degrees if summing by columns
            in_range = cv.transpose(in_range)
            self._selected = cv.transpose(self._selected)

        # use the coordinates of the selected elements to get the rows to iterate over
        coordinates = np.where(in_range > 0)
        selected_rows = np.unique(coordinates[0], return_counts=True)

        # sum the differences between the max and min value along the chosen axis
        i, area_px = 0, 0
        for count, row in zip(selected_rows[1], selected_rows[0]):

            # the array is ordered, so the first element will be the min and the last will be the max
            x_max, x_min = coordinates[1][i:i+count][-1], coordinates[1][i:i+count][0]
            dist = x_max - x_min + 1  # add one to account for "starter pixel"
            area_px += dist
            i += count

            # fill in the row on the image to show what we're calculating
            fill_color = self.area_color if not fill_color else fill_color
            self._selected[row, x_min:x_max] = np.full((dist-1, 3), fill_color)

        return area_px * self.px_size if not return_pixels else area_px


if __name__ == "__main__":
    print("\n-------------------\nPlease run main.py!")
