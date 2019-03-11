'''
An example of a multilayer perceptron using Keras,  for theDeep Learning workshop.

We will use the MNIST dataset of handwritten digits (http://yann.lecun.com/exdb/mnist/)

Authors: Eduardo Matallanas (@matallanas)
Pablo Doval (@PabloDoval)
'''
import sys
sys.path.append('../') 
import keras as k
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from utils.init import init

if __name__ == '__main__':
    init()
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Set up parameters, etc..
 

    # Prepare data


    # Build model (using the softmax activation function)


    # Train the model


    # Evaluate it against the test dataset


    print('Train loss: ', xxxx)
    print('Train accuracy: ', xxxx)
