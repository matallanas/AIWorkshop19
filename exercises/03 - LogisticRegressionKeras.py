'''
A very simple example of logistic regression via using Keras this time, used for the
Deep Learning workshop.

We will use the MNIST dataset of handwritten digits (http://yann.lecun.com/exdb/mnist/)

Authors: Eduardo Matallanas (@matallanas)
Pablo Doval (@PabloDoval)
'''
import sys
sys.path.append('../') 
import keras as k
from keras.datasets import mnist
import numpy as np
from utils.init import init

if __name__ == '__main__':
    init()

    # Retrieve dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Set up parameters and hyper-parameters


    # Prepare data: Resoze and normalize, as well set outcomes as categorical
 

    # Build model (using the softmax activation function)


    # Train the model
 

    # Evaluate it against the test dataset

    print('Train loss: ', xxxx)
    print('Train accuracy: ', xxxx)
