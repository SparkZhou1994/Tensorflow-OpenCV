# 1 样本 2 训练 3 预测
# 1 样本
# 1.1 pos 正样本 包含所检测目标 neg 不包含obj 正样本尽量多样 环境 干扰 pos:neg = 1:2 或 1:3
# 视频转图片 等比缩放 裁剪 64x128
# 2 训练
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1 参数设置 2 hog 3 svm 4 computer hog 5 label 6 train 7 pred 8 draw

# 1 参数设置
PosNum = 820
NegNum = 1931
winSize = (64,128)
blockSize = (16,16) # 105
blockStride = (8,8) # 4 cell
cellSize = (8,8)
nBin = 9 # 9 bin 3780

# 2 创建hog
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBin)

# 3 创建svm
svm = cv2.ml.SVM_create()

# 4 计算hog
featureNum = int(((128-16)/8+1)*((64-16)/8+1)*4*9)
featureArray = np.zeros(((PosNum+NegNum),featureNum),np.float32)
labelArray = np.zeros(((PosNum+NegNum),1),np.int32)

# 5 设置label
# 正样本 设置 label
for i in range(0,PosNum):
    fileName = 'pos/'+str(i+1)+'.jpg'
    img = cv2.imread(fileName)
    hist = hog.compute(img,(8*8))
    for j in range(0,featureNum):
        featureArray[i,j] = hist[j]
    labelArray[i,0] = 1
# 负样本 设置 label
for i in range(0,NegNum):
    fileName = 'neg/'+str(i+i)+'jpg'
    img = cv2.imread(fileName)
    for j in range(0,featureNum):
        featureArray[i+PosNum,j] = hist[j]
    labelArray[i+PosNum,0] = -1
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

# 6 train
ret = svm.train(featureArray,cv2.ml.ROW_SAMPLE,labelArray)

#7 pred
alpha = np.zeros((1),np.float32)
rho = svm.getDecisionFunction(0,alpha)
print(rho)
print(alpha)
alphaArray = np.zeros((1,1),np.float32)
supportVArray = np.zeros((1,featureNum),np.float32)
resultArray = np.zeros((1,featureNum),np.float32)
alphaArray[0,0] = alpha
resultArray = -1*alphaArray*supportVArray
# detect
myDetect = np.zeros((3781),np.float32)
for i in range(0,3780):
    myDetect[i] = resultArray[0,i]
myDetect[3780] = rho[0] # 判决用
# 创建hog
myHog = cv2.HOGDescriptor()
myHog.setSVMDetector(myDetect)

imageSrc = cv2.imread('Test2.jpg',1)# load
objs = myHog.detectMultiScale(imageSrc,0,(8,8),(32,32),1.05,2) # 检测
x = int(objs[0][0][0])
y = int(objs[0][0][1])
w = int(objs[0][0][2])
h = int(objs[0][0][3])

#8 draw
cv2.rectangle(imageSrc,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('dst',imageSrc)
cv2.waitKey(0)





