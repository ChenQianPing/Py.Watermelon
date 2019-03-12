import tensorflow as tf
import numpy as np

a02 = tf.constant([1,2,3,4],dtype=tf.float32)

# 创建会话
sess = tf.InteractiveSession()

print(sess.run(tf.norm(a02, ord='euclidean')))  # 5.477226
print(np.sqrt(1*1+2*2+3*3+4*4)) # 477225575051661


a03 = tf.constant([[1,2],[3,4]],dtype=tf.float32)
print(a03)   # Tensor("Const_1:0", shape=(2, 2), dtype=float32)

print(sess.run(a03))

# [[1. 2.]
#  [3. 4.]]

print(sess.run(tf.norm(a03,ord=2)))  # 5.477226

print(sess.run(tf.norm(a03,ord=1)))  # 10.0

print(sess.run(tf.norm(a03,ord=np.inf)))  # 4.0




