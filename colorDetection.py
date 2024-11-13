import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)


while True:

    # Grab camera feed
    isValid, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_bound = np.array([100, 150, 0])
    upper_bound = np.array([140, 255, 255])
    # Display camera feed
    # cv.imshow('frame', hsv )

    mask = cv.inRange(hsv, lower_bound , upper_bound)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', result)
    # Wait 1s then wait to see if "q' is pressed, if pressed kill loop
    if cv.waitKey(1) == ord('q'):
        break

# Release camera back to other programs if needed
capture.release()