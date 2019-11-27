# 7-1 7-12
# 样本地址 http://yann.lecun.com/exdb/mnist/
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
# 1 load data
# 2 knn test train distance 5*500 = 2500 784=28*28
# 3 knn k个最近的图片5 500 1-》 500 train(4)
# 4 k个最近的图片 -> parse centent label
# 5 label -> 数字
# 6 检测概率统计
# load data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# 属性设置
trainNum = 55000
testNum = 10000
trainSize = 500
testSize = 5
k = 4

# data 分解
trainIndex = np.random.choice(trainNum,trainSize,replace=False)
testIndex = np.random.choice(testNum,testSize,replace=False)
trainData = mnist.train.images[trainIndex] # 训练图片
trainLabel = mnist.train.labels[trainIndex] # 训练标签
testData = mnist.test.images[testIndex] # 测试图片
testLabel = mnist.test.labels[testIndex] # 测试标签
print('trainData.shape=',trainData.shape) # 500*784 1 图片个数 2 像素点
print('trainLabel.shape=',trainLabel.shape)

# tf input
trainDataInput = tf.placeholder(shape=[None,784],dtype=tf.float32)
trainLabelInput = tf.placeholder(shape=[None,10],dtype=tf.float32)
testDataInput = tf.placeholder(shape=[None,784],dtype=tf.float32)
testLabelInput = tf.placeholder(shape=[None,10],dtype=tf.float32)

#knn distance
f1 = tf.expand_dims(testDataInput,1) # 维度扩展 5*785 -> 5*1*784
f2 = tf.subtract(trainDataInput,f1) # 784 sum(784)
f3 = tf.reduce_sum(tf.abs(f2),reduction_indices=2) # 完成数据累加 5*500
f4 = tf.negative(f3) # 取反
f5,f6 = tf.nn.top_k(f4,k=4) # 选取f4 最大的四个值 即f3 最小的四个值
f7 = tf.gather(trainLabelInput,f6)
f8 = tf.reduce_sum(f7,reduction_indices=1) #f8 sum
f9 = tf.argmax(f8,dimension=1) #f8最大值的下标

with tf.Session() as sess:
    p1 = sess.run(f1,feed_dict={testDataInput:testData[0,5]})
    print('p1=',p1.shape) # (5,1,784)
    p2 = sess.run(f2,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5]})
    print('p2=',p2.shape) # (5,500,784)
    p3 = sess.run(f3,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5]})
    print('p3=',p3.shape) # (5,500)
    p4 = sess.run(f4,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5]})
    print('p4=',p4.shape) # (5,500)
    p5,p6 = sess.run((f5,f6),feed_dict={trainDataInput:trainData,testDataInput:testData[0,5]})
    print('p5=',p5.shape) #(5,4)
    print('p6=',p6.shape) #(5,4)
    p7 = sess.run(f7,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5],trainLabelInput:trainLabel})
    print('p7=',p7.shape) #(5,4,10)
    p8 = sess.run(f8,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5],trainLabelInput:trainLabel})
    print('p8=',p8.shape) #(5,10)
    p9 = sess.run(f9,feed_dict={trainDataInput:trainData,testDataInput:testData[0,5],trainLabelInput:trainLabel})
    print('p9=',p9.shape) #(5,)
    p10 = np.argmax(testLabel[0:5],axis=1)
    print('p10[]=',p10)

j = 0
for i in range(0,5):
    if p10[i] == p9[i]:
        j = j + 1
print('ac=',j*100/5)
