#!/bin/bash

# Usage: ./script.sh DATASET_NUMBER INT_LIST
# Example: ./script.sh 18 "1 2 4 6 7 9 11 13 14 16"

DATASET_NUMBER=$1
INT_LIST=$2

# Define the base path
BASE_PATH="/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp"


# Third command
cd "${BASE_PATH}" &&
python scripts/run.py --scene "${BASE_PATH}/data/nerf/dataset_${DATASET_NUMBER}/train/110_13051_23361_infer" --n_steps 20000 --save_snapshot "${BASE_PATH}/data/nerf/dataset_${DATASET_NUMBER}/train/110_13051_23361_infer/110_13051_23361_infer.ingp" --test_transforms "${BASE_PATH}/data/nerf/test_psnr/test_${DATASET_NUMBER}_infer/transforms.json" --int_list $INT_LIST --save_gif "test_infer_${DATASET_NUMBER}" 