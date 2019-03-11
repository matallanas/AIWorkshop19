'''
A TensorFlow 'hello world', performing a very basic operation, to explain 
the concepts of the session, operators, etc.

Authors: Eduardo Matallanas (@matallanas)
Pablo Doval (@PabloDoval)
'''
import sys
sys.path.append('../') 
import tensorflow as tf
from utils.init import init, TF_LOGGING_FOLDER

if __name__ == '__main__':
    init()
   
    # --- CONSTANT OPERATORS ---
    # Step 1: Let's define a couple of constant operators here

    
    # Step 2: Create a session where to perform addition and multiplication of
    # the ops
    

    # --- PLACEHOLDERS---
    # Step 1: Define two int16 placeholders so we can operate with them later
    

    # Step 2: Define our addition and multiplication operationss
    
    # Step 3: Create a session for these operations


    # -- MATRIXES ---
    # Step 1: Define two constant matrixes. The fiest one, 1x2, while the 
    # second is 2x1
    
    # Step 2: Define the matrix multiplication

    # Step 3: Create a session for these operations

    # --- DEBUG ---
    # Step 1: Create a session for the previous multiplication, but writing the
    # output to the tensorflow log.
    
    # Step 2: Analyze the graph with TensorBoard
    