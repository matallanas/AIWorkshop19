'''
A simple smoke test for the environment set up for the Deep Learning workshop.
This code ensures the user will be able to run Keras and TensorFlow, outputs the 
versions of each package and list the GPUs supported on the machine, if any.

Authors: Eduardo Matallanas (@matallanas)
Pablo Doval (@PabloDoval)
'''

import sys
sys.path.append('../') 

from utils.init import init, get_available_gpus
import tensorflow as tf
import keras


if __name__ == '__main__':
    init()

    # Print TensorFlow and Keras versions

    # Print the GPUs available in the system
    print("List of available GPUs: ")
    print(get_available_gpus())
