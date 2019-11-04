# 4-5 颜色反转(彩色图片)
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0,height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        dst[i, j] = (255-b, 255-g, 255-r)
cv2.imshow('dst', dst)
cv2.waitKey(0)