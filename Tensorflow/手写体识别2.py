import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 载入数据集
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def max_pool(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')

x = tf.placeholder(tf.float32, [None, 784])
x_image = tf.reshape(x, [-1, 28, 28, 1])

k = 4
l = 8
m = 12

W1 = tf.Variable(tf.truncated_normal([5,5,1,k],stddev = 0.1))
b1 = tf.Variable(tf.ones([k])/10)

W2 = tf.Variable(tf.truncated_normal([5,5,k,l],stddev = 0.1))
b2 = tf.Variable(tf.ones([l])/10)

W3 = tf.Variable(tf.truncated_normal([5,5,l,m],stddev = 0.1))
b3 = tf.Variable(tf.ones([m])/10)

n = 200

W4 = tf.Variable(tf.truncated_normal([1*1*m,n],stddev = 0.1))
b4 = tf.Variable(tf.ones([n])/10)

W5 = tf.Variable(tf.truncated_normal([n,10],stddev = 0.1))
b5 = tf.Variable(tf.ones([10])/10)

y1 = tf.nn.relu(tf.nn.conv2d(x_image,W1,strides=[1,1,1,1],padding = 'SAME')+b1)
print(y1.shape)
y1 = max_pool(y1)
print(y1.shape)

y2 = tf.nn.relu(tf.nn.conv2d(y1,W2,strides=[1,2,2,1],padding = 'SAME')+b2)
print(y2.shape)
y2 = max_pool(y2)
print(y2.shape)

y3 = tf.nn.relu(tf.nn.conv2d(y2,W3,strides=[1,2,2,1],padding = 'SAME')+b3)
print(y3.shape)
y3 = max_pool(y3)
print(y3.shape)

yy = tf.reshape(y3,shape=[-1,1*1*m])

y4 = tf.nn.relu(tf.matmul(yy,W4)+b4)
print(y4.shape)

y = tf.nn.softmax(tf.matmul(y4, W5) + b5)
print(y.shape)

# 为了计算交叉熵，我们首先需要添加一个新的占位符用于输入正确值
y_ = tf.placeholder("float", [None, 10])

# 交叉熵损失函数
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

#训练方法，学习率为1e-4
train_step = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)

#初始化变量
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# 开始训练模型,循环训练1000次
for i in range(20000):
    # 随机抓取训练数据中的100个批处理数据点
    batch_xs, batch_ys = mnist.train.next_batch(100)

    # 喂入数据，开始训练
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    if(i%100 == 0):
        print("train step is : "+str(i))
        #计算正确率
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# 检验真实标签与预测标签是否一致
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 计算精确度，将true和false转化成相应的浮点数，求和取平均
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# 计算所学习到的模型在测试数据集上面的正确率
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


# 训练了20000轮，读者可以将训练轮数在加倍，正确率会更高 0.9741
