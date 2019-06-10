'''
The first Neural Network implementation in Keras, used for the Deep Learning workshop.
We will use the MNIST dataset of handwritten digits (http://yann.lecun.com/exdb/mnist/)

Authors: Pablo Doval (@PabloDoval)
'''

import sys
sys.path.append('../') 
from utils.init import init
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, Activation
import keras as k
from utils.init import init
from keras.utils import np_utils

if __name__ == '__main__':
    init()
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    height = X_train.shape[1]
    width = X_train.shape[2]
    num_test = X_test.shape[0]
    num_classes = 10
    training_epochs = 20
    batch_size = 50
    num_train = X_train.shape[0]
    input_shape = (height, width, 1)
    pool_size = (3,3)

    #prepare data
    X_train = X_train.reshape(num_train, width, height, 1)
    X_test = X_test.reshape(num_test, width, height, 1)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255
    Y_train = k.utils.to_categorical(y_train, num_classes)
    Y_test = k.utils.to_categorical(y_test, num_classes)


    # Model definition
    model = Sequential()
    model.add(Conv2D(8, (5, 5), padding = 'valid', input_shape = input_shape))
    model.add(Activation('sigmoid'))
    model.add(Conv2D(12, (3, 3)))
    model.add(Activation('sigmoid'))
    model.add(Flatten())
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    # Compilation step
    model.compile(loss = 'categorical_crossentropy', optimizer = 'adadelta',metrics = ['accuracy'])
    model.fit(X_train,
            Y_train, 
            batch_size = batch_size, 
            epochs = training_epochs, 
            verbose = 1, 
            validation_data = (X_test, Y_test))

    # Evaluate it against the test dataset
    score = model.evaluate(X_test, Y_test, verbose=True)

    print('Train loss: ', score[0])
    print('Train accuracy: ', score[1])
    