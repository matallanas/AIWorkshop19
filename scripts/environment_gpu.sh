#!/bin/bash
conda env create --file ../anaconda_env_gpu.yml
if [ $? -ne 0 ]
then
    echo '[ERROR]: Something wrong happened during the creation of the environment.';
else
    conda activate aiworkshop
fi
