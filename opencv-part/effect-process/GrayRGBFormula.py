# 4-3 方法4 gray = r*0.299 + g*0.587 + b*0.114
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(0,height):
    for j in range(0,width):
        (b,g,r) = img[i,j]
        gray = int(b)*0.114+int(g)*0.587+int(r)*0.299
        dst[i,j] = np.uint8(gray)
cv2.imshow('dst',dst)
cv2.waitKey(0)