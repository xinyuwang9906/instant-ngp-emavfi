#!/bin/bash

# Usage: ./script.sh DATASET_NUMBER INT_LIST
# Example: ./script.sh 18 "1 2 4 6 7 9 11 13 14 16"

DATASET_NUMBER=$1


# Define the base path
BASE_PATH="/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp"


# Second command colmap for infer test
cd "${BASE_PATH}/data/nerf/test_psnr/test_${DATASET_NUMBER}_infer" &&
python "${BASE_PATH}/scripts/colmap2nerf.py" --run_colmap --aabb_scale 16 --images "${BASE_PATH}/data/nerf/test_psnr/test_${DATASET_NUMBER}_infer" 

