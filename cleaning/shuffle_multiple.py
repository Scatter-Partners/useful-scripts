import os
import glob
import json
import random
import shutil

# Seed for randomness
random.seed(12345)  # change this number if you want a different random order

# Base directories, the input folder should have multiple folders that each has an images/json folders pair
input_base_dir = "input"
output_dir = "output"

# Ensure output directories exist
os.makedirs(os.path.join(output_dir, "json"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

def process_folder(subfolder):
    # Construct paths to JSON and image subdirectories
    json_path = os.path.join(input_base_dir, subfolder, "json")
    image_path = os.path.join(input_base_dir, subfolder, "images")

    # Verify directories exist
    assert os.path.isdir(json_path), f"The directory '{json_path}' does not exist"
    assert os.path.isdir(image_path), f"The directory '{image_path}' does not exist"

    # Find all JSON and image files
    json_files = [jf for jf in glob.glob(os.path.join(json_path, "*")) if not jf.endswith('.DS_Store')]
    image_files = [ifile for ifile in glob.glob(os.path.join(image_path, "*")) if not ifile.endswith('.DS_Store')]

    # Create dictionaries with basename (without extension) as keys and full path as values
    json_files_dict = {os.path.splitext(os.path.basename(jf))[0]: jf for jf in json_files}
    image_files_dict = {os.path.splitext(os.path.basename(ifile))[0]: ifile for ifile in image_files}

    # Ensure matching sets of JSON and image files
    assert set(json_files_dict.keys()) == set(image_files_dict.keys()), "The JSON and image file names should match"

    # Create list of (json_file, image_file) pairs
    pairs = [(json_files_dict[key], image_files_dict[key]) for key in json_files_dict.keys()]
    return pairs

# List all subfolders in the input directory
subfolders = [f.name for f in os.scandir(input_base_dir) if f.is_dir()]

all_pairs = []
for subfolder in subfolders:
    pairs = process_folder(subfolder)
    all_pairs.extend(pairs)

# Shuffle the combined list of pairs
random.shuffle(all_pairs)

# Process all shuffled pairs
for i, (json_file, image_file) in enumerate(all_pairs, start=1):
    # Load JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Update JSON fields
    data["name"] = f"Name #{i}"
    filename, file_extension = os.path.splitext(data['image'])
    file_extension = file_extension or '.png'  # default to .png if no extension found
    data["image"] = f"ipfs://REPLACEME/{i}{file_extension}"

    for key in ["imageHash", "dna", "edition", "date", "custom_fields", "file_url", "id",
                "seller_fee_basis_points", "compiler", "properties", "collection"]:
        data.pop(key, None)

    # Save the updated JSON
    with open(os.path.join(output_dir, "json", f"{i}"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Copy the corresponding image
    shutil.copy(image_file, os.path.join(output_dir, "images", f"{i}{file_extension}"))
