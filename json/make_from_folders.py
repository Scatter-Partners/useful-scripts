import os
import shutil
import json
import re
import random

# Config
START_INDEX = 1  # put your starting index here
INPUT_FOLDER = 'input'  # put your input folder here
OUTPUT_FOLDER = 'output'  # put your output folder here
SHUFFLE_OUTPUT = True  # set to True to shuffle output
RANDOM_SEED = 123  # set the seed for random number generation
SUBFOLDERS_WITHOUT_ID = ['User Bonklers']  # put your subfolder names here to not add IDs
IPFS_CID = 'REPLACEME'
NAME_PREFIX = 'Name'
FILE_TYPE = '.png'

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Created directory: {directory}')

def create_json(index, collection, original_id, file_extension, output_folder=OUTPUT_FOLDER):
    data = {
        "name": f"{NAME_PREFIX} #{index}",
        "image": f"ipfs://{IPFS_CID}/{index}{file_extension}",
        "description": "Description.",
        "external_url": "https://scatter.art",
        "attributes": [
            {
                "trait_type": "Collection",
                "value": f"{collection}"
            }
        ]
    }
    if collection not in SUBFOLDERS_WITHOUT_ID:
        data["attributes"].append({
            "trait_type": f"{collection} ID",
            "value": f"{original_id}"
        })
    
    with open(f'{output_folder}/json/{index}', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    print(f'Created JSON file: {output_folder}/json/{index}')

def process_images():
    current_index = START_INDEX
    ensure_dir(f'{OUTPUT_FOLDER}/images')
    ensure_dir(f'{OUTPUT_FOLDER}/json')

    for root, dirs, files in os.walk(INPUT_FOLDER):
        for dir in dirs:
            for file in os.listdir(os.path.join(root, dir)):
                if file.endswith(FILE_TYPE):
                    original_id, _ = os.path.splitext(file)  # get filename without extension
                    shutil.copy2(os.path.join(root, dir, file), f'{OUTPUT_FOLDER}/images/{current_index}{FILE_TYPE}')
                    print(f'Copied image: {os.path.join(root, dir, file)} to {OUTPUT_FOLDER}/images/{current_index}{FILE_TYPE}')
                    create_json(current_index, dir, original_id, FILE_TYPE)
                    current_index += 1

    if SHUFFLE_OUTPUT:
        random.seed(RANDOM_SEED)  # set the seed
        shuffle_folder = f'{OUTPUT_FOLDER}_shuffled'
        ensure_dir(f'{shuffle_folder}/images')
        ensure_dir(f'{shuffle_folder}/json')

        indices = list(range(START_INDEX, current_index))
        random.shuffle(indices)

        for old_index, new_index in zip(range(START_INDEX, current_index), indices):
            shutil.copy2(f'{OUTPUT_FOLDER}/images/{old_index}{FILE_TYPE}', f'{shuffle_folder}/images/{new_index}{FILE_TYPE}')
            print(f'Copied image: {OUTPUT_FOLDER}/images/{old_index}{FILE_TYPE} to {shuffle_folder}/images/{new_index}{FILE_TYPE}')

            with open(f'{OUTPUT_FOLDER}/json/{old_index}', 'r', encoding='utf-8') as infile:
                data = json.load(infile)

            data["name"] = f"{NAME_PREFIX} #{new_index}"
            data["image"] = re.sub(r'(\d+)', str(new_index), data["image"])

            create_json(new_index, data["attributes"][0]["value"], data["attributes"][1]["value"] if len(data["attributes"]) > 1 else '', FILE_TYPE, shuffle_folder)

process_images()
