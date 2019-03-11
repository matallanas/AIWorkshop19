# Workshop Inteligencia Artificial - Microsoft Educación 

## Initial Setup

1. First of all, please do install Anaconda 5.3 in your machine

    * Windows version [here](https://repo.continuum.io/archive/Anaconda3-5.3.0-Windows-x86_64.exe).
    * Linux version [here](https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh).
    * MacOS X version [here](https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh).

2. Go to the .\Scripts folder and run the script that will perform the environment setup:
    * environment.bat (if you are running Windows)
    * ./environment.sh (for you, Linux folks)

3. Once the script finishes running, that environment will be active. The name of the environment is *aitech18-deeplearningworkshop*, in case you want to activate it manually.

4. If you plan on using GPU - and you should! - install the CUDA toolkit from [this link](https://developer.nvidia.com/cuda-toolkit) to the NVIDIA web page.

5. Run the *main.py* to check that the environment and dependencies have been properly setup. The output will show the version of the Tensorflow and Keras distributions, as well as the number of CPUs and GPUs available in our machine.

## Sample Data Sets

The workshop will use the following datasets:

* MNIST Hand Written Digits

The data is not provided in this repo, but instead needs to be downloaded and processed sepparately. These can be downloaded, and have the needed transformations applied automatically, by running the following Python command from the base directory:

`python scripts/retrieve_datasets.py`

Both datasets are described to a greater extent in the next sections:

## Mnist Handwritten Digits Database

The initial exercises of this workshop will use the MNIST Handwritten Digits database; this publicly available dataset has become a sort of *de facto* industry standard to test the performance of certain image classification algorithms. Even though a detailed description of this data set is not intended here (more information [here](https://en.wikipedia.org/wiki/MNIST_database)), suffice to say that each image represents a handwrittend digit, from 0 to 9, as an array of 9x9 pixels.

![MNIST image sample](http://3.bp.blogspot.com/_UpN7DfJA0j4/TJtUBWPk0SI/AAAAAAAAABY/oWPMtmqJn3k/s1600/mnist_originals.png)

## Authors

* Eduardo Matallanas de Ávila - @matallanas
* Jose Fernández Vizoso - @jvizoso
* Pablo Álvarez Doval - @PabloDoval
