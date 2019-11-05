# 4-17
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
height = int(img.shape[0]*0.2)
width = int(img.shape[1]*0.2)
imgResize = cv2.resize(img,(width,height))
for i in range(0,height):
    for j in range(0,width):
        img[i+200,j+350] = imgResize[i,j]
cv2.imshow('src',img)
cv2.waitKey(0)