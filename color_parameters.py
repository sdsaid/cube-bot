import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 
import imutils 
#from transform import four_point_transform


#import image 
img = cv.imread('/Users/saiddahirsaid/Desktop/flat_cube.png')

#resize image
ratio = img.shape[0] / 500.0
orig = img.copy()
img = imutils.resize(img, height = 500)

#convert bgr to hsv and gray. gray is for edge detection
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray,(3,3),0)
#canny edge detection to find contours 
edges = cv.Canny(gray, 80, 200)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


#color parameters
lower_white = np.array([0, 0, 0])
upper_white = np.array([0, 0, 255])

lower_blue = np.array([110, 100, 70])
upper_blue = np.array([130,255,255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

#orange
lower_orange = np.array([15, 100, 50])
upper_orange = np.array([20, 255, 255])

#green 
lower_green = np.array([50,60,60])
upper_green = np.array([90,255, 255])

#red wraps around hsv, needing two masks. theres probably a better way but idk
#lower red mask
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])
#mask0 = cv.inRange(hsv, lower_red, upper_red)
lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])
#mask1 = cv.inRange(hsv, lower_red, upper_red)


#color masks
white_mask = cv.inRange(hsv, lower_white, upper_white)
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
yellow_mask = cv.inRange(hsv, lower_yellow, upper_yellow)
orange_mask = cv.inRange(hsv, lower_orange, upper_orange)
green_mask = cv.inRange(hsv, lower_green, upper_green)
mask0 = cv.inRange(hsv, lower_red, upper_red)
mask1 = cv.inRange(hsv, lower_red, upper_red)

red_mask = mask0+mask1

#combine all masks
masks = white_mask+blue_mask+yellow_mask+orange_mask+green_mask+red_mask
mask = cv.bitwise_or(masks, masks)


def facelets():


























#find contours, and sort them by size
contours = cv.findContours(edges.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours
cnt = imutils.grab_contours(cnt)
cnt = sorted(cnt, key = cv.contourArea, reverse = True)

#contour size parameters
for c in cnt:
	perimeter = cv.arcLength(c,True)
	epsilon = 0.1* perimeter
	approx = cv.approxPolyDP(c,epsilon,True)


	#once we find rectangle, we break 
	if len(approx) == 4 and is  blue_mask:
		screenCnt = approx 


img = cv.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)

'''
#use four point transform module 
transformed = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio ) 
transformed = imutils.resize(transformed, height = 500)
'''

#geometric transformation 
#save as new image
cv.imshow('img', img)
#cv.imshow('edges', edges)
#cv.imshow('transformed', transformed)
cv.waitKey(0)
cv.destroyAllWindows()

