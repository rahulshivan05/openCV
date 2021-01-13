import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photo/10.jpeg')
cv.imshow('Original', img)

# plt.imshow(img)
# plt.show()


# RGB to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("HSV-----> BGR", lab_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)