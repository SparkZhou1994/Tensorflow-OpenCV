# 3-3
# 最近临域插值 双线性插值 原理
# 最近临域插值
# dst x 1 -> src x 2 newX
# newX = x*(src 行/目标行)
# newX = 1*(10/5) = 2
# 12.3 = 12

# 双线性插值
# 1 最终点 = A1 30% + A2 70%
# 2 最终点 = B1 20% + B2 80%

# 3-4
import cv2
import numpy as np
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height/2)
dstWidth = int(width/2)
dstImage = np.zeros((dstHeight,dstWidth,3),np.uint8)
for i in range(0,dstHeight):
    for j in range(0,dstWidth):
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i,j] = img[iNew,jNew]
cv2.imshow('dst',dstImage)
cv2.waitKey(0)
# 1 opencv API resize 2 算法原理 3 源码10