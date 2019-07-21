import numpy as np
import cv2 

#video capture device 
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()			#take each frame
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	#conver BGR to HSV 

	#define the upper and lower values for BLUE in HSV
	lower_blue = np.array([110, 100, 70]) 
	upper_blue = np.array([130,255,255])

	lower_orange = np.array([10, 50, 50])
	upper_orange = np.array([15, 255, 255])

	lower_green = np.array([50,60,60])
	upper_green = np.array([90,255, 255])

	lower_red = np.array([[0, 70, 50], [170, 70, 50]])
	upper_red = np.array([[10, 255, 255], [180, 255, 255]])

	#threshold the HSV image for each color 
	mask1 = cv2.inRange(hsv, lower_orange, upper_orange)
	mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
	mask3 = cv2.inRange(hsv, lower_green, upper_green)

	#bitwise and mask over original image 
	mask = cv2.bitwise_or(mask2, mask3 )
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

#close windows
cap.release()
cv2.destroyAllWindows()