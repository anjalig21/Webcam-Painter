import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

# Initializing Webcam
cap = cv2.VideoCapture(0)

# Width = ID #3, Height = ID #4, Brightness = ID #10
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Hue_min/max, Sat_min/max, Value_min/max,
myColours = [[96, 10, 75, 116, 182, 167],
             [43, 0, 49, 90, 182, 120],
             [147, 81, 93, 179, 147, 156],
             [16, 100, 93, 31, 255, 160]]


# Values are in BGR not RGB
myColourValues = [[204, 204, 0],
                  [0, 153, 0],
                  [204, 0, 204],
                  [0, 255, 255]]


# [x, y, colourID]
myPoints = []


# Used to recognize colour and track points for drawing
def findColour(img, myColours, myColourValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    counter = 0
    newPoints = []
    for colour in myColours:
        lower = np.array(colour[0:3])
        upper = np.array(colour[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(imgResult, (np.float32(x), np.float32(y)), 15, myColourValues[counter], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, counter])
        counter += 1
    return newPoints


# Used to find tip of pen
def get_contours(img):
    # cv2.RETR_EXTERNAL good to find outer corners/details
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area_og = int(cv2.contourArea(cnt))
        if area_og > 50:
            area = int(cv2.contourArea(cnt))
            perimeter = int(cv2.arcLength(cnt, True))
            # Calculates vertices
            approx_points = cv2.approxPolyDP(cnt, 0.02*(perimeter), True)
            # gives x, y, width and height of all shapes
            x, y, w, h = cv2.boundingRect(approx_points)
    return x+w/2, y


# Used to draw all points
def draw(myPoints, myColourValues):
    for point in myPoints:
        cv2.circle(imgResult, (np.float32(point[0]), np.float32(point[1])),
                   5, myColourValues[point[2]], cv2.FILLED)


while True:
    _, image = cap.read(0)
    img = cv2.flip(image, 1)
    imgResult = img.copy()
    newPoints = findColour(img, myColours, myColourValues)
    if len(newPoints) != 0:
        for newpt in newPoints:
            myPoints.append(newpt)
    if len(myPoints) != 0:
        draw(myPoints, myColourValues)
    cv2.imshow("Result", imgResult)

    # if 'q' is pressed, webcam turns off
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
