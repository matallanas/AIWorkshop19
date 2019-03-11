'''
This file holds the basic initialization and setup functions, as well as a set
of project-wide constants for settings.

Authors: Eduardo Matallanas (@matallanas)
'''
import os
import tensorflow as tf
from tensorflow.python.client import device_lib
from tensorflow import logging


# Project-wide constants
MNIST_DATA_FOLDER = '../datasets/mnistdata/files/'
TF_LOGGING_FOLDER = '../log/'
TF_LOGGING_VERBOSITY = logging.DEBUG

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

def setup_logging():
    # Set the verbosity as defined in the init constants
    tf.logging.set_verbosity(TF_LOGGING_VERBOSITY)

def init():
    # Disables the warning for the AVX/FMA extensions
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    # Set up the TensorFlow logging
    setup_logging()