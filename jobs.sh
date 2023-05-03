#!/bin/bash

source .bashrc
conda deactivate
conda activate edcs
rm -f /Users/frdrck/edcs/edcs/.data/edcs/data.zip

python /Users/frdrck/edcs/edcs/edcs_export/data.py
#/home/frdrck/miniconda3/envs/edcs/bin/python /home/frdrck/edcs/edcs_export/data.py