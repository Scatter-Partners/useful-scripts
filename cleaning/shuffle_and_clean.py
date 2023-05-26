import os
import glob
import json
import random
import shutil

# Seed for randomness
random.seed(1234) # change this number if you want a different random order

# Directories
input_dir = "input"
output_dir = "output"

# Verify input directories exist
assert os.path.isdir(os.path.join(input_dir, "json")), "The directory 'input/json' does not exist"
assert os.path.isdir(os.path.join(input_dir, "images")), "The directory 'input/images' does not exist"

# Find all JSON and image files
json_files = [jf for jf in glob.glob(os.path.join(input_dir, "json", "*")) if not jf.endswith('.DS_Store')]
image_files = [ifile for ifile in glob.glob(os.path.join(input_dir, "images", "*.png")) if not ifile.endswith('.DS_Store')]

# Create dictionaries with basename (without extension) as keys and full path as values
json_files_dict = {os.path.splitext(os.path.basename(jf))[0]: jf for jf in json_files}
image_files_dict = {os.path.splitext(os.path.basename(ifile))[0]: ifile for ifile in image_files}

# Make sure the number of JSON and image files are the same
assert set(json_files_dict.keys()) == set(image_files_dict.keys()), "The JSON and image file names should match"

# Create output directories if they don't exist
os.makedirs(os.path.join(output_dir, "json"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

# Create a list of pairs (json_file, image_file)
pairs = [(json_files_dict[key], image_files_dict[key]) for key in json_files_dict.keys()]
random.shuffle(pairs)

# Process the pairs
for i, (json_file, image_file) in enumerate(pairs, start=1):
    # Load JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Update JSON fields
    data["name"] = f"Name #{i}"
    data["image"] = f"ipfs://REPLACEME/{i}.png"
    #data["description"] = "uncomment to add  description if you desire"
    
    for key in ["imageHash", "dna", "edition", "date", "custom_fields", "file_url", "id", 
                "seller_fee_basis_points", "compiler", "properties", "collection", "external_url"]:
        data.pop(key, None)
            
    # Save the updated JSON
    with open(os.path.join(output_dir, "json", f"{i}"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Copy the corresponding image
    shutil.copy(image_file, os.path.join(output_dir, "images", f"{i}.png"))
