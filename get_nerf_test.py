import os
import shutil
import argparse
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame', default='18', type=int)
    args = parser.parse_args()
    return args

def process_images(infer_dir, output_test_dir):
    # Check if output directory exists, create if not
    if not os.path.exists(output_test_dir):
        os.makedirs(output_test_dir)
    else:
        # If exists, clear all files in the directory
        for file in os.listdir(output_test_dir):
            file_path = os.path.join(output_test_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    all_images = sorted([f for f in os.listdir(infer_dir) if os.path.isfile(os.path.join(infer_dir, f))])
    selected_images = all_images[::4]

    for img in selected_images:
        shutil.move(os.path.join(infer_dir, img), output_test_dir)

    new_infer_images = sorted([f for f in os.listdir(infer_dir) if os.path.isfile(os.path.join(infer_dir, f))])

    if len(os.listdir(output_test_dir)) < 25:
        print("Selecting new images to be added to test")
        indices = np.round(np.linspace(0, len(new_infer_images) - 1, min(20, len(new_infer_images)))).astype(int)
        additional_images = [new_infer_images[i] for i in indices]
        copied_files = []

        for img in additional_images:
            shutil.copy(os.path.join(infer_dir, img), output_test_dir)
            copied_files.append(img)

        # Save copied file names to a text file
        with open(f'copied_files_{args.frame}.txt', 'w') as file:
            for img in copied_files:
                file.write(img + '\n')

        # Print image names and indices
        sorted_output_images = sorted(os.listdir(output_test_dir))
        all_indices = []
        for img in copied_files:
            index = sorted_output_images.index(img)
            all_indices.append(index)
            print(f"Copied Image Name: {img}, Index in Test Folder: {index}")
        print("All indices in sorted folder:", all_indices)

if __name__ == "__main__":
    args = get_args()
    
    infer_folder = f"/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp/data/nerf/dataset_{args.frame}/train/110_13051_23361_infer"
    output_test_folder = f"/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp/data/nerf/test_psnr/test_{args.frame}_infer"
    process_images(infer_folder, output_test_folder)
