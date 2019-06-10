'''
A very simple example of logistic regression via Keras this time, used for the
Deep Learning workshop.

We will use the MNIST dataset of handwritten digits (http://yann.lecun.com/exdb/mnist/)

Authors: Pablo Doval (@PabloDoval)
'''
import sys
sys.path.append('../') 
import keras as k
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import TensorBoard
import numpy as np
from utils.init import init

if __name__ == '__main__':
    init()
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Set a few variables to use later
    num_train = X_train.shape[0]
    height = X_train.shape[1]
    width = X_train.shape[2]
    num_test = X_test.shape[0]
    num_classes = 10
    training_epochs = 20
    batch_size = 50

    # Prepare data
    X_train = X_train.reshape(num_train, height * width)
    X_test = X_test.reshape(num_test, height * width)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255
    Y_train = k.utils.to_categorical(y_train, num_classes)
    Y_test = k.utils.to_categorical(y_test, num_classes)

    # Build model (using the softmax activation function)
    model = Sequential()
    model.add(Dense(num_classes, activation = 'softmax', input_dim = height * width))
    model.compile(loss = 'categorical_crossentropy', optimizer = 'SGD', metrics = ['accuracy'])

    tensorboard = TensorBoard(log_dir = './log', 
                              histogram_freq = 1,  
                              write_graph = True, 
                              write_images = True)

    # Train the model
    model.fit(X_train, 
            Y_train, 
            batch_size = batch_size, 
            epochs = training_epochs, 
            verbose = True, 
            validation_split = 0.1, 
            callbacks = [tensorboard])

    # Evaluate it against the test dataset
    score = model.evaluate(X_test, Y_test, verbose = True)

    print('Train loss: ', score[0])
    print('Train accuracy: ', score[1])
