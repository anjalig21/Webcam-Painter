import numpy as np
import cv2
from collections import deque

# Defining upper and lower bounds for a colour to be considered Orange
orangeLower = np.array([100, 60, 60])
orangeUpper = np.array([140, 255, 255])

# Defining a matrix to add pixels to the boundaries of objects in an image (dilation)
# and to remove pixels on object boundaries (erosion).
matrix = np.ones((5,5)), np.uint8)

# Initialize different deques to store colours in arrays
blue = [deque(maxlen=512)]
green = [deque(maxlen=512)]
red = [deque(maxlen=512)]
yellow = [deque(maxlen=512)]

#Initialize index variable for all colours
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# Blue, Green, Red, Yellow respectively
colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colourIndex = 0