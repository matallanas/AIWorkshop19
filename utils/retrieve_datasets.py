'''
This module will deal with download the required datasets for the workshop.

Authors: Eduardo Matallanas (@matallanas)
'''
import sys
sys.path.append('../') 
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from utils.init import MNIST_DATA_FOLDER, TF_LOGGING_VERBOSITY

if __name__ == '__main__':
    
    # Set the verbosity to ERROR. This is to avoid the warnings of the MNIST
    # download.
    tf.logging.set_verbosity(tf.logging.ERROR)

    # Perform the download itself
    mnist = input_data.read_data_sets(MNIST_DATA_FOLDER, one_hot=True)
    
    # Set the verbosity as defined in the init constants
    tf.logging.set_verbosity(TF_LOGGING_VERBOSITY)  