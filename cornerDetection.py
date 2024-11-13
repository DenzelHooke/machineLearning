import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)


while True:

    # Grab camera feed
    source = cv.imread('assets/chessboard.jpg')
    grayscale = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(grayscale, 8, 0.1, 10)

    # Returns array as int valued instead rather than float
    corners = np.int_(corners)

    for corner in corners:
        print(corner)
        x, y = corner.ravel()

        image = cv.circle(source, (x, y), 20, (0, 0, 255), -1)

    for i in range(len(corners)):
        for x in range(i + 1, len(corners)):
            corner1 = corners[i][0]
            corner2 = corners[x][0]

            cv.line(source, corner1, corner2, (255, 0, 0))


    print(corners)
    cv.imshow('frame', image)
    # Wait 1s then wait to see if "q' is pressed, if pressed kill loop
    if cv.waitKey(1) == ord('q'):
        break

# Release camera back to other programs if needed
capture.release()