import time
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
with tf.Session() as sess:
    sess.run(hello)
    a = tf.constant(10)
    b = tf.constant(32)
    sess.run(a+b)
//    while True:
//        time.sleep(5)
