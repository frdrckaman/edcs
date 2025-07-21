#!/usr/bin/env bash
set -euo pipefail

# —— adjust this to wherever your Conda is installed ——
CONDA_BASE=/home/live/miniconda3

# 1) load conda functions for non-interactive shells
if [ -f "$CONDA_BASE/etc/profile.d/conda.sh" ]; then
    # this gives you `conda activate`
    . "$CONDA_BASE/etc/profile.d/conda.sh"
else
    echo "ERROR: cannot find conda.sh at $CONDA_BASE/etc/profile.d/conda.sh" >&2
    exit 1
fi

# 2) check & activate your EDCS env
if ! conda env list | grep -qE '^[[:space:]]*live[[:space:]]'; then
    echo "ERROR: conda env 'live' not found." >&2
    echo "Available envs:" >&2
    conda env list >&2
    exit 1
fi
conda activate live

# 3) ensure we have a python on $PATH
PYTHON=$(command -v python) || true
if [ -z "$PYTHON" ]; then
    echo "ERROR: python not found even after conda activate." >&2
    exit 1
fi

# 4) cleanup old exports
#rm -f /home/live/edcs/.data/edcs/data.zip
#rm -f /home/live/edcs/.data/edcs/data/*.xlsx

# 5) run your Django-export job
cd /home/live/edcs/edcs_export
#"$PYTHON" data.py
python data.py