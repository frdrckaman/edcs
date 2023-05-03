#!/bin/bash

conda deactivate
conda activate edcs
rm -f /Users/frdrck/edcs/edcs/.data/edcs/data.zip
source python /home/frdrck/edcs/edcs/edcs_export/data.py