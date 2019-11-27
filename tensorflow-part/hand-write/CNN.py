# 7-13
# CNN
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# load data
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# input
imageInput = tf.placeholder(tf.float32,[None,784]) # 28*28
labelInput = tf.placeholder(tf.float32,[None,10]) #knn

# data reshape
imageInputReshape = tf.reshape(imageInput,[-1,28,28,1]) # [None,784] -> M*28*28*1 2D->4D 28*28 wh 1 channel

# 卷积
w0 = tf.Variable(tf.truncated_normal([5,5,1,32],stddev=0.1)) #权重 卷积内核 5*5 out:32 in 1
b0 = tf.Variable(tf.constant(0.1,shape=[32]))
# layer1:激励函数 + 卷积运算
# imageInputReshape: M*28*28*1 w0:5,5,1,32
layer1 = tf.nn.relu(tf.nn.conv2d(imageInputReshape,w0,strides=[1,1,1,1],padding='SAME')+b0)
# M*28*28*32
layer1_pool = tf.nn.max_pool(layer1,ksize=[1,4,4,1],strides=[1,4,4,1],padding='SAME') #pool 下采样 数据量减少很多 M*28*28*32 =>M*7*7*32
# [1,2,3,4] -> [4]

# layer2:out: softmax(激励函数 + 乘加运算)        softmax为回归函数
w1 = tf.Variable(tf.truncated_normal([7*7*32,1024],stddev=0.1))
b1 = tf.Variable(tf.constant(0.1,shape=[1024]))
h_reshape = tf.reshape(layer1_pool,[-1,7*7*32])
h1 = tf.nn.relu(tf.matmul(h_reshape,w1)+b1)

# softMax
w2 = tf.Variable(tf.truncated_normal([1024,10],stddev=0.1))
b2 = tf.Variable(tf.constant(0.1,shape=[10]))
pred = tf.nn.softmax(tf.matmul(h1,w2)+b2)

loss0 = labelInput*tf.log(pred)
loss1 = 0
for m in range(0,100): # test 100
    for n in range(0,10):
        loss1 = loss1 - loss0[m,n]
loss = loss1/100

# train
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(500):
        images,labels = mnist.train.next_batch(500)
        sess.run(train,feed_dict={imageInput:images,labelInput:labels})

        pred_test = sess.run(pred,feed_dict={imageInput:images,labelInput:labels})
        acc = tf.equal(tf.arg_max(pred_test,1),tf.arg_max(mnist.test.labels,1))
        acc_float = tf.reduce_mean(tf.cast(acc,tf.float32))
        acc_result = sess.run(acc_float,feed_dict={imageInput:mnist.test.images,labelInput:mnist.test.labels})
        print(acc_result)

