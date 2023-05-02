import os
import glob
import json
import random
import shutil

# Directories
input_dir = "input"
output_dir = "output"

# Find all JSON and image files
json_files = glob.glob(os.path.join(input_dir, "json", "*"))
image_files = glob.glob(os.path.join(input_dir, "images", "*.png"))

# Make sure the number of JSON and image files are the same
print(len(json_files), len(image_files))
assert len(json_files) == len(image_files), "The number of JSON and image files should be the same"

# Create output directories if they don't exist
os.makedirs(os.path.join(output_dir, "json"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

# Create a list of pairs (json_file, image_file)
pairs = list(zip(json_files, image_files))
random.shuffle(pairs)

# Process the pairs
for i, (json_file, image_file) in enumerate(pairs, start=1):
    # Load JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Update JSON fields
    data["name"] = f"Name #{i}"
    data["image"] = f"ipfs://REPLACEME/{i}.png"
    
    if "imageHash" in data:
        del data["imageHash"]
    if "dna" in data:
        del data["dna"]
    if "edition" in data:
        del data["edition"]
    if "date" in data:
        del data["date"]
    if "custom_fields" in data:
        del data["custom_fields"]
    if "file_url" in data: #not actually part of JSON format https://docs.opensea.io/docs/metadata-standards
        del data["file_url"]
    if "id" in data:
        del data["id"]
    if "seller_fee_basis_points" in data:
        del data["seller_fee_basis_points"]
    if "compiler" in data:
        del data["compiler"]
    if "properties" in data:
        del data["properties"]
    if "collection" in data:
        del data["collection"]
    if "external_url" in data:
        del data["external_url"]           

    # Save the updated JSON
    with open(os.path.join(output_dir, "json", f"{i}"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Copy the corresponding image
    shutil.copy(image_file, os.path.join(output_dir, "images", f"{i}.png"))
