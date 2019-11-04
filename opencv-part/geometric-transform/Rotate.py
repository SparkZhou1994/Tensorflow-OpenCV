# 3-12 图片旋转
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),45,0.5)
dst = cv2.warpAffine(img,matRotate,(height,width))
cv2.imshow('dst',dst)
cv2.waitKey(0)