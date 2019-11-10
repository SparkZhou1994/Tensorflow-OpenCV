# 6-2 视频分解图片
import cv2
cap = cv2.VideoCapture("E:/1.mp4")
isOpened = cap.isOpened()
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
i = 0
while(isOpened):
    if i == 10:
        break;
    else:
        i = i+1
    (flag,frame) = cap.read()
    fileName = 'E:/image' + str(i) + '.jpg'
    if flag == True:
        cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])