import json
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame', default='18', type=int)
    args = parser.parse_args()
    return args


def get_indices_of_images_in_txt(json_file_path, txt_file_path):
    # Load JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Load image names from the txt file
    with open(txt_file_path, 'r') as txt_file:
        images_in_txt = [line.strip() for line in txt_file.readlines()]

    # Iterate over frames and check if image is in txt file
    indices = []
    file_names = []
    count = 0
    for i, frame in enumerate(data['frames']):
        file_name = frame['file_path'].split('/')[-1]  # Extract the file name from the path
        print(file_name)
        if file_name in images_in_txt:
            indices.append(i)
            file_names.append(file_name)
        count+=1

    print(f"there are {count} frames in total, {len(file_names)} are repeated")
    return indices


if __name__ == "__main__":
    args = get_args()
        
    # Define file paths
    json_file_path = f'/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp/data/nerf/test_psnr/test_{args.frame}_infer/transforms.json'
    txt_file_path = f'/home/iam-loki/Documents/XinyuWang/16824/project/instant-ngp/copied_files_{args.frame}.txt'

    # Get indices
    indices = get_indices_of_images_in_txt(json_file_path, txt_file_path)
    print(" ".join(map(str, indices)))