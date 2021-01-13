import cv2 as cv

img = cv.imread('photo/7.jpg')
cv.imshow('Nature', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Dilating the images
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow("Dilated", dilated)

# Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow("Eroded", eroded)

# Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow("Resized", resized)

# Cropping
# cropped = img[50:200, 200:400]
# cv.imshow("Crop Image", cropped)

cv.waitKey(0)