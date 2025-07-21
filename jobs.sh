#!/bin/bash

source /home/live/.bashrc

eval "$(/home/live/miniconda3/bin/conda shell.bash hook)"

conda deactivate
conda activate edcs

rm -f /home/live/edcs/.data/edcs/data.zip
rm -f /home/live/edcs/.data/edcs/data/*.xlsx

cd /home/live/edcs/edcs_export

python data.py