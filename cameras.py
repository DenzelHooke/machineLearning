import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)


while True:

    # Grab camera feed
    isValid, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = smaller_frame
    image[:height//2, width//2:width] = smaller_frame
    image[height//2:height, :width//2] = smaller_frame
    image[height//2:height, width//2:width] = smaller_frame

    # Display camera feed
    cv.imshow('frame', image)


    # Wait 1s then wait to see if "q' is pressed, if pressed kill loop
    if cv.waitKey(1) == ord('q'):
        break

# Release camera back to other programs if needed
capture.release()