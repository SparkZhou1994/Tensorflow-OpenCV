# 5-5 灰度直方图 源码
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('E:/wallpaper/1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
count = np.zeros(256,np.float)
for i in range(0,height):
    for j in range(0,width):
        pixel = gray[i,j]
        index = int(pixel)
        count[index] = count[index]+1
for i in range(0,255):
    count[i] = count[i]/(height*width)
x = np.linspace(0,255,256)
y = count
plt.bar(x,y,alpha=1,color='b')
plt.show()
cv2.waitKey(0)
