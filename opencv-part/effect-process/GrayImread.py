# 4-2 灰度处理 方式1 imread
import cv2
img0 = cv2.imread('E:/wallpaper/1.jpg',0)
img1 = cv2.imread('E:/wallpaper/1.jpg',1)
print(img0.shape)
print(img1.shape)
cv2.imshow('src',img0)
cv2.waitKey(0)