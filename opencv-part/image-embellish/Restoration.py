# 5-4 图片修补
import cv2
import numpy as np
def createDamagedImage():
    img = cv2.imread('E:/wallpaper/1.jpg',1)
    for i in range(200,300):
        img[i,200] = (255,255,255)
        img[i,200+1] = (255,255,255)
        img[i,200-1] = (255,255,255)
    for i in range(150,250):
        img[250,i] = (255,255,255)
        img[250+1, i] = (255, 255, 255)
        img[250-1, i] = (255, 255, 255)
    cv2.imwrite('E:/wallpaper/3.jpg',img)

createDamagedImage()
img = cv2.imread('E:/wallpaper/3.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
paint = np.zeros((height,width,1),np.uint8)
for i in range(200, 300):
    paint[i, 200] = 255
    paint[i, 200 + 1] = 255
    paint[i, 200 - 1] = 255
for i in range(150, 250):
    paint[250, i] = 255
    paint[250 + 1, i] = 255
    paint[250 - 1, i] = 255
cv2.imshow('paint',paint)
# 1 src 2 mask
imgDst =cv2.inpaint(img,paint,3,cv2.INPAINT_TELEA)
cv2.imshow('dst',imgDst)
cv2.waitKey(0)