# 8-4
import cv2

# 1 load xml file name
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('haarcascade_eye.xml')

# 2 load jpg
img = cv2.imread('face.jpg')
cv2.imshow('src',img)

# 3 haar gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 4 detect
faces = face_xml.detectMultiScale(gray,1.3,5)
print('face=',len(faces))

# dram
index = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_face = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    fileName = str(index)+'.jpg'
    cv2.imwrite(fileName,roi_color)
    index = index + 1