# 5-3 彩色 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
cv2.imshow('src',img)
(b,g,r) = cv2.split(img) # 通道分解
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH,gH,rH)) # 通道合成
cv2.imshow('dst',result)
cv2.waitKey(0)