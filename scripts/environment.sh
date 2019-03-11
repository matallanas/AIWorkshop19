# !/bin/bash
conda-env create --file ../anaconda_env.yml
if [ $? -ne 0 ]
then
    echo '[ERROR]: Something wrong happened during the creation of the environment.';
else
    source activate aiworkshop
fi
