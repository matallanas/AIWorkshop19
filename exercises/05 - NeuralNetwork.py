'''
The first Neural Network implementation in Keras, used for the Deep Learning workshop.
We will use the MNIST dataset of handwritten digits (http://yann.lecun.com/exdb/mnist/)

Authors: Eduardo Matallanas (@matallanas)
Pablo Doval (@PabloDoval)
'''

import sys
sys.path.append('../') 
from utils.init import init
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras as k
from utils.init import init
from keras.utils import np_utils

if __name__ == '__main__':
    init()
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Set up parameters, etc..
    

    # Prepare data


    # Model definition

    # Compilation step

    # Evaluate it against the test dataset

    print('Train loss: ', xxxx)
    print('Train accuracy: ', xxxx)
    