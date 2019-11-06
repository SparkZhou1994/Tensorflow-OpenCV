# 5-3 灰度 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('src',img)
dst = cv2.equalizeHist(gray)
cv2.imshow('dst',dst)
cv2.waitKey(0)