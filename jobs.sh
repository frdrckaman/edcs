#!/bin/bash
PATH=/home/live/miniconda3/envs/live/bin:/home/live/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

conda deactivate
conda activate edcs
rm -f /home/live/edcs/.data/edcs/data.zip
rm -f /home/live/edcs/.data/edcs/data/*.xlsx

python /home/live/edcs/edcs_export/data.py