# CSCI B550 - Project 1
Developed by Hunter Boyd
## About the Project
This project implements a simple class, [AreaEstimator](#areaestimator), to estimate the area of an irregular, contiguous shape in an image - 
specifically PartyRockFire.jpeg.
This may work to estimate the area of other images, but it has been tailored to this one. 
This software works best on objects with clear, single-colored borders and few appendages.

## AreaEstimator
AreaEstimator is the main class of the project and does almost all of the work.
Below is my description of the class found in calculatearea.py.

    
    A class that can estimate the area of contiguous shapes based on a colored outline.
    It also provides a visual representation of the estimated area.
    
    AreaEstimator has four inputs, all have a default for Project 1:

    Parameters:
    -----------
        :param filename: name and filepath of the image file to load
        :param feet_per_pixel: the ratio of feet to pixels
        :param color_range: the minimum and maximum BGR colors that will be picked up by cv.inRange
        :param area_color: the color used to fill in the estimated area - not related to calculation
    

## Dependencies
This project was developed using:
* Python version: 3.9.6
* numpy version: 1.21.2
* opencv-python version: 4.5.3.56
	
## Setup

To run this project, make sure `main.py`, `calculatearea.py`, and  `PartyRockFire.jpeg` are all in the same directory.

Next, install the dependencies using pip:

```
$ python -m pip install numpy
$ python -m pip install opencv-python
```
or using requirements.txt (installs above modules)
```
$ pythom -m pip install -r requirements.txt
```

Then run main.py to calculate the area.
```
$ python main.pye
```