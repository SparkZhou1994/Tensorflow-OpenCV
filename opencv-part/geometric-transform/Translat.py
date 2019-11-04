# 3-6 translat
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matShift = np.float([[1,0,100],[0,1,200]]) # 2*3
dst = cv2.warpAffine(img,matShift,(height,width))
cv2.imshow('dst',dst)
cv2.waitKey(0)