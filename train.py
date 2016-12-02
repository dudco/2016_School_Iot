import tensorflow as tf
import numpy as np

xy = np.loadtxt("handhaker_train.txt",unpack=True)
x_data = np.transpose(xy[0:5])
y_data = np.transpose(xy[5:])

# print (x_data)
# print (y_data)

X = tf.placeholder(tf.float32, shape=[None, 5],name='X-input')
Y = tf.placeholder(tf.float32, shape=[None, 5], name='Y-input')

W1 = tf.get_variable("Weight1", shape=[5, 5],initializer=tf.contrib.layers.xavier_initializer())
W2 = tf.get_variable("Weight2", shape=[5, 10],initializer=tf.contrib.layers.xavier_initializer())
W3 = tf.get_variable("Weight3", shape=[10, 5],initializer=tf.contrib.layers.xavier_initializer())
W4 = tf.get_variable("Weight4", shape=[5, 15],initializer=tf.contrib.layers.xavier_initializer())
W5 = tf.get_variable("Weight5", shape=[15, 30],initializer=tf.contrib.layers.xavier_initializer())
W6 = tf.get_variable("Weight6", shape=[30, 10],initializer=tf.contrib.layers.xavier_initializer())
W7 = tf.get_variable("Weight7", shape=[10, 5],initializer=tf.contrib.layers.xavier_initializer())

b1 = tf.Variable(tf.zeros([5]),name="Bias1")
b2 = tf.Variable(tf.zeros([10]),name="Bias2")
b3 = tf.Variable(tf.zeros([5]),name="Bias3")
b4 = tf.Variable(tf.zeros([15]),name="Bias4")
b5 = tf.Variable(tf.zeros([30]),name="Bias5")
b6 = tf.Variable(tf.zeros([10]),name="Bias6")
b7 = tf.Variable(tf.zeros([5]),name="Bias7")

param_list = [W1, b1, W2, b2, W3, b3, W4, b4, W5, b5, W6, b6, W7, b7]
saver = tf.train.Saver(param_list)


L2 = tf.nn.tanh(tf.add(tf.matmul(X, W1),b1))
L3 = tf.nn.tanh(tf.add(tf.matmul(L2, W2), b2))
L4 = tf.nn.tanh(tf.add(tf.matmul(L3, W3), b3))
L5 = tf.nn.tanh(tf.add(tf.matmul(L4, W4), b4))
L6 = tf.nn.tanh(tf.add(tf.matmul(L5, W5), b5))
L7 = tf.nn.tanh(tf.add(tf.matmul(L6, W6), b6))
hypothesis = tf.sigmoid(tf.add(tf.matmul(L7, W7),b7))


with tf.name_scope('cost') as scope:
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))

with tf.name_scope('train') as scope:
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(cost)


init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for step in range(20001):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step%200 == 0:
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}))
            saver.save(sess, './iot.ckpt')

    a = sess.run(hypothesis, feed_dict={X:[[213, 175, 188, 285, 76]]})
    print("a : ", a, sess.run(tf.arg_max(a, 1)))
