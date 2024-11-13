import cv2 as cv
import numpy as np

img = cv.imread('assets/highway.jpg', -1)


# .shape returns basic image data such as height, width and channels if image is 3d(rgb) in a tuple like (1920, 1080, 3).

print(img.shape)

# Create a black line for top half of image
# for row in range(350):
#     for pixelColumn in range(img.shape[1]):
#         img[row][pixelColumn] = [0, 0, 255]


copy = img[400:700, 0: 300]
upsidedown = []


# Flip image upside down

for row in range(299, 0, -1):
    # print(row)
    upsidedown.append(copy[row])


# print(copy[299][0][0])
# print(upsidedown)
img[250:549, 350:650] = upsidedown


# print()



cv.imshow('balllllz ', img)

cv.waitKey(0)

cv.destroyAllWindows()

