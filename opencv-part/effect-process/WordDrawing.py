# 4-17
import cv2
img = cv2.imread('E:/wallpaper/1.jpg',1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img,(200,100),(500,400),(0,255,0),3)
cv2.putText(img,'this is flow',(100,300),font,1,(200,100,255),2,cv2.LINE_AA)
cv2.imshow('src',img)
cv2.waitKey(0)