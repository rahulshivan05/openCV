import cv2 as cv

def rescaleFrame(frame, scale=0.75):
	# Images, Videos and Live Videos
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
	# Live Videos
	capture.set(3, width)
	capture.set(4, height)

img = cv.imread('photo/1.jpg')

cv.imshow('2', img)
resized_image = rescaleFrame(img)
cv.imshow("Images", resized_image)


cv.waitKey(0)


# Reading Video
# capture = cv.VideoCapture('video/video.mp4')

# while True:
# 	isTrue, frame = capture.read()

# 	frame_resized = rescaleFrame(frame, scale=.2)

# 	cv.imshow('Video', frame)
# 	cv.imshow("Video Resize", frame_resized)

# 	if cv.waitKey(20) & 0xff==ord('d'):
# 		break

# capture.release()
cv.destroyAllWindows()















