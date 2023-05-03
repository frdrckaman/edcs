#!/bin/bash

source /home/frdrck/.bashrc
conda deactivate
conda activate edcs
rm -f /home/frdrck/edcs/.data/edcs/data.zip

python /home/frdrck/edcs/edcs_export/data.py
#/home/frdrck/miniconda3/envs/edcs/bin/python /home/frdrck/edcs/edcs_export/data.py