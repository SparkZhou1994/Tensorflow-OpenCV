# 4-10
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# newP = gray0 - gray1 + 150
dst = np.zeros((height,width,1),np.uint8)
for i in range(0,height):
    for j in range(0,width-1):
        grayP0 = int(gray[i,j])
        grayP1 = int(gray[i,j+1])
        newP = grayP0 - grayP1 + 150
        if newP > 255:
            newP = 255
        if newP < 0:
            newP = 0
        dst[i,j] = newP
cv2.imshow('dst',dst)
cv2.waitKey(0)
