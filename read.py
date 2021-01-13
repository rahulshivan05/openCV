import cv2 as cv

img = cv.imread('photo/1.jpg')

cv.imshow('1', img)
cv.waitKey(0)

# Reading Video
# capture = cv.VideoCapture('video/video.mp4')

# while True:
# 	isTrue, frame = capture.read()
# 	cv.imshow('Video', frame)

# 	if cv.waitKey(20) & 0xff==ord('d'):
# 		break

# capture.release()
# cv.destroyAllWindows()

