#!/bin/bash
PATH=/home/frdrck/miniconda3/envs/edcs/bin:/home/frdrck/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

#source /home/frdrck/.bashrc
conda deactivate
conda activate edcs
rm -f /home/frdrck/edcs/.data/edcs/data.zip

python /home/frdrck/edcs/edcs_export/data.py
#/home/frdrck/miniconda3/envs/edcs/bin/python /home/frdrck/edcs/edcs_export/data.py