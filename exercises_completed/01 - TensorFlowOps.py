'''
A TensorFlow 'hello world', performing a very basic operation, to explain 
the concepts of the session, operators, etc.

Authors: Pablo Doval (@PabloDoval)
'''
import sys
sys.path.append('../') 
import tensorflow as tf
from utils.init import init, TF_LOGGING_FOLDER

if __name__ == '__main__':
    init()
   
    # --- CONSTANT OPERATORS ---

    op1 = tf.constant(10)
    op2 = tf.constant(15)

    # Create a session for these operations
    with tf.Session() as sess:
        print("Addition with constants: %i" % sess.run(op1+op2))
        print("Multiplication with constants: %i" % sess.run(op1*op2))

    # --- PLACEHOLDERS---

    op1 = tf.placeholder(tf.int16)
    op2 = tf.placeholder(tf.int16)

    # Define our operations
    add = tf.add(op1, op2)
    mul = tf.multiply(op1, op2)

    # Create a session for these operations
    with tf.Session() as sess:
        print("Addition with variables: %i" % sess.run(add, feed_dict={op1: 10, op2: 15}))
        print("Multiplication with variables: %i" % sess.run(mul, feed_dict={op1: 10, op2: 15}))
    
    # -- MATRIXES ---
    
    matrix1 = tf.constant([[10., 10.]])
    matrix2 = tf.constant([[15.],[15.]])

    product = tf.matmul(matrix1, matrix2)

    # Create a session for these operations
    with tf.Session() as sess:
        result = sess.run(product)
        print(result)

    # --- DEBUG ---
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(TF_LOGGING_FOLDER, sess.graph)

        result = sess.run(product)
        print(result)

        writer.close()
    