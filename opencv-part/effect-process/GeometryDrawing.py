# 4-15
import cv2
import numpy as np
newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo,np.uint8)
# line
cv2.line(dst,(100,100),(400,400),(0,0,255))
# line weight
cv2.line(dst,(100,200),(400,200),(0,255,255),20)
# line type
cv2.line(dst,(100,300),(400,300),(0,255,0),20,cv2.LINE_AA)
# triangle
cv2.line(dst,(200,150),(50,250),(25,100,255))
cv2.line(dst,(50,250),(400,380),(25,100,255))
cv2.line(dst,(50,255),(400,380),(25,100,255))
# 4-16 rectangle
cv2.rectangle(dst,(50,100),(200,300),(255,0,0),-1)
# circle
cv2.circle(dst,(250,250),(50),(0,255,0),2)
# ellipse
cv2.ellipse(dst,(256,256),(150,100),0,0,180,(255,255,0),-1)
# polygon
points = np.array([[150,50],[140,140],[200,170],[250,250],[150,50]],np.uint32)
points = points.reshape((-1,1,2))
cv2.polylines(dst,[points],True,(0,255,255))
cv2.imshow('dst',dst)
cv2.waitKey(0)