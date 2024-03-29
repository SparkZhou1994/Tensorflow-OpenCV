# 5-3 YUV 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgYUV = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow('src',img)
channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channels = cv2.merge(channelYUV)
result = cv2.cvtColor(channels,cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst',result)
cv2.waitKey(0)