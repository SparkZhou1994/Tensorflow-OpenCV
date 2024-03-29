# 5-9
# p = p + 40
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
dst = np.zeros((height,width,3),np.uint8)
for i in range(0,height):
    for j in range(0,width):
        (b,g,r) = img[i,j]
        bb = int(b)+40
        gg = int(g)+40
        rr = int(r)+40
        if bb > 255:
            bb = 255
        if gg > 255:
            gg = 255
        if rr > 255:
            rr =255
        dst[i,j] = (bb,gg,rr)
cv2.imshow('dst',dst)
cv2.waitKey(0)