# 5-10
# 双边滤波 磨皮美白
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
cv2.imshow('src',img)
dst = cv2.bilateralFilter(img,15,35,35)
cv2.imshow('dst',dst)
cv2.waitKey(0)