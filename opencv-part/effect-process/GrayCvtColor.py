# 方法2 cvtColor
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('dst',dst)
cv2.waitKey(0)