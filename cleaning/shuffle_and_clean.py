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

# Find all JSON and image files
json_files = glob.glob(os.path.join(input_dir, "json", "*"))
image_files = glob.glob(os.path.join(input_dir, "images", "*.png"))

# Create dictionaries with basename as keys and full path as values
json_files_dict = {os.path.basename(jf).split(".")[0]: jf for jf in json_files}
image_files_dict = {os.path.basename(iff).split(".")[0]: iff for iff in image_files}

# Make sure the number of JSON and image files are the same
assert set(json_files_dict.keys()) == set(image_files_dict.keys()), "The JSON and image file names should match"

# Create output directories if they don't exist
os.makedirs(os.path.join(output_dir, "json"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

# Create a list of pairs (json_file, image_file)
pairs = list(zip(json_files_dict.values(), image_files_dict.values()))
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