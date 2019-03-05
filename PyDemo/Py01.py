# 引入 TensorFlow 模块
import tensorflow as tf

# 创建一个整型常量，即 0 阶 Tensor
t0 = tf.constant(3, dtype=tf.int32)

# 创建一个浮点数的一维数组，即 1 阶 Tensor
t1 = tf.constant([3., 4.1, 5.2], dtype=tf.float32)

# 创建一个字符串的2x2数组，即 2 阶 Tensor
t2 = tf.constant([['Apple', 'Orange'], ['Potato', 'Tomato']], dtype=tf.string)

# 创建一个 2x3x1 数组，即 3 阶张量，数据类型默认为整型
t3 = tf.constant([[[5], [6], [7]], [[4], [3], [2]]])

# 打印上面创建的几个 Tensor
# print(t0)
# print(t1)
# print(t2)
# print(t3)

# print 一个 Tensor 只能打印出它的属性定义，并不能打印出它的值，要想查看一个 Tensor 中的值还需要经过Session 运行一下
sess = tf.Session()
# print(sess.run(t0))
# print(sess.run(t1))
# print(sess.run(t2))
# print(sess.run(t3))


# g1 = tf.linspace(1.0,10.0,16)
# print(g1)
#
# g2 = tf.constant(sess.run(tf.reshape(g1,[4,4])))
# print(g2)
#
# print(sess.run(g2))

# g7 = tf.zeros([4,5])
# print(sess.run(g7))
#
# g8 = tf.zeros([10,10],dtype=tf.int32)
# print(sess.run(g8))
#
# g9 = tf.ones([8,2],dtype=tf.int64)
# print(sess.run(g9))
#
#
# g10 = tf.fill([5,5],10.1)
# print(sess.run(g10))
#
# g11 = tf.diag([1, 1, 2, 2])
# print(sess.run(g11))
#
# g11 = tf.diag([1, 1, 2, 2])
# g12 = tf.diag_part(g11)
# print(sess.run(g12))
# print(g12)
#
# g13 = tf.random_normal([5, 5])
# print(sess.run(g13))

# g14 = tf.random_normal([3,8], mean=1.0, stddev=2.0, dtype=tf.float32)
# print(sess.run(g14))
#
# g1 = tf.linspace(1.0,10.0,16)
# g2 = tf.constant(sess.run(tf.reshape(g1,[4,4])))
# g3 = tf.transpose(g2)
# print(g3)
# print(sess.run(g3))
#
# g4 = tf.linspace(1.0, 10.0, 6)
# g5 = tf.reshape(g4,[2,3])
# print(sess.run(g5))
#
# g6 = tf.constant(sess.run(tf.transpose(g5)))
# print(sess.run(g6))


# h01 = tf.random_normal([4,4])
# h02 = tf.fill([4,4],1.0)
# print(sess.run(h02))
#
# h04 = h02 + 2.0
# print(sess.run(h04))
#
# h05 = tf.reshape(tf.linspace(1.0,10.0,16),[4,4])
# h06 = tf.reshape(tf.linspace(1.0,16.0,16),[4,4])
# print(h05 @ h06)
# print(sess.run(h05 @ h06))
#
# i01 = tf.diag([1.0,2.0,3.0,4.0])
# print(sess.run(i01))
#
# i01_rev = tf.matrix_inverse(i01)
# print(sess.run(i01_rev))
#
# print(sess.run(i01_rev @ i01))
# print(sess.run(i01 @ i01_rev))

# A1 = [[1,1,1],[1,-1,-1],[5,-2,2]]
# A = tf.constant(A1, tf.float32)
# print(A)
# print(sess.run(A))
#
# d = tf.matrix_determinant(A)
# print(sess.run(d))

# A1 = [[1,1,1],[1,-1,-1],[5,-2,2]]
# A = tf.constant(A1, tf.float32)
# b = tf.constant([[1],[2],[3]],dtype=tf.float32)
# print(b)
# print(sess.run(b))
#
# print(sess.run(tf.matmul(tf.matrix_inverse(A),b)))

# x+y+z =1,
# x-y-z =2,
# 5x-2y+2z =3

A1 = [[3,2],[3.5,3.6]]
A = tf.constant(A1, tf.float32)
b = tf.constant([[118.4],[135.2]],dtype=tf.float32)
print(b)
print(sess.run(b))

print(sess.run(tf.matmul(tf.matrix_inverse(A),b)))

# A1 = [[1,1,1],[1,-1,-1],[5,-2,2]]
# A = tf.constant(A1, tf.float32)
# b = tf.constant([[9],[1],[21]],dtype=tf.float32)
# print(b)
# print(sess.run(b))
#
# print(sess.run(tf.matmul(tf.matrix_inverse(A),b)))

