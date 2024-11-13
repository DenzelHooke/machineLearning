import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)


while True:

    # Grab camera feed
    isValid, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))




    # frame, starting pos, end pos, line color, thickness.
    img = cv.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv.line(frame, (0, height), (width, 0), (255, 0, 0), 10)
    cv.circle(frame, (0,0), 10, (255, 255, 255))

 /   # Display camera feed
    cv.imshow('frame', img)

    # Wait 1s then wait to see if "q' is pressed, if pressed kill loop
    if cv.waitKey(1) == ord('q'):
        break

# Release camera back to other programs if needed
capture.release()