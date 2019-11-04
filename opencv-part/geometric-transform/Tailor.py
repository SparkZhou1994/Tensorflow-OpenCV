# 3-5 tailor
# 100 -> 200 x
# 100 -> 300 y
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
dst = img[100:200,100:300]
cv2.imshow('image',dst)
cv2.waitKey(0)