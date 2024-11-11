import os
import requests
import zipfile
import shutil

def download_and_extract(url, output_folder):
    print("downloading ", url)
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Download the file
    response = requests.get(url)
    zip_file_path = os.path.join(output_folder, 'temp.zip')

    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    
    # Unzip the file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)
    
    # Remove the zip file
    os.remove(zip_file_path)
    print("download done")

# Pretrain (feature alignment)
# Download https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain as liuhaotian/LLaVA-Pretrain
# dataset = load_dataset("liuhaotian/LLaVA-Pretrain", split="train", cache_dir="LLaVA/playground/data/llava_pretrain")
# os.system('./pretrain.sh')

# Visual Instruction Tuning
# Download the JSON file
json_url = 'https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain/resolve/main/blip_laion_cc_sbu_558k.json'
json_response = requests.get(json_url)

with open('../playground/data/blip_laion_cc_sbu_558k.json', 'wb') as f:
    f.write(json_response.content)
print("done here")

# https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain/resolve/main/images.zip
download_and_extract('https://huggingface.co/datasets/liuhaotian/LLaVA-Pretrain/resolve/main/images.zip', '../playground/data/llava_pretrain/')

# json_url = 'https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K/resolve/main/llava_v1_5_mix665k.json'
# json_response = requests.get(json_url)

# with open('../playground/data/llava_v1_5_mix665k.json', 'wb') as f:
#     f.write(json_response.content)

# # Download COCO dataset
# download_and_extract('http://images.cocodataset.org/zips/train2017.zip', '../playground/data/coco/train2017')

# # Download GQA images
# download_and_extract('https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip', '../playground/data/gqa/images')

# # Download OCR-VQA images
# ocr_vqa_folder = './playground/data/ocr_vqa/images'
# os.makedirs(ocr_vqa_folder, exist_ok=True)
# # cd ./playground/data/ocr_vqa/images
# # from this: https://drive.google.com/drive/folders/1_GYPY5UkUy7HIcR0zq3ZCFgeZN7BAfm_
# # 1. import dataset.json into folder
# # 2. run loadDataset.py

# # Download TextVQA images
# download_and_extract('https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip', './playground/data/textvqa/train_images')

# # Download VisualGenome part 1
# download_and_extract('https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip', './playground/data/vg/VG_100K')

# # Download VisualGenome part 2
# download_and_extract('https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip', './playground/data/vg/VG_100K_2')

# Training
# os.system('./finetune.sh')
# If not enough GPU memory: os.system('./finetune_lora.sh')
