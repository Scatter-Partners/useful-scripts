import sys
import json
import os

# Usage: python generate_json_no_traits.py <cid_hash_image> <output_folder> <image_filename> <supply>

if len(sys.argv) < 5:
    print("Insufficient arguments provided.")
    print("Usage: python generate_json_no_traits.py <cid_hash_image> <output_folder> <image_filename> <supply>")
    sys.exit(1)

cid_hash_image = sys.argv[1]
output_folder = sys.argv[2]
image_filename = sys.argv[3]
supply = int(sys.argv[4])

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'Created folder: "{output_folder}"')

for x in range(1, supply + 1):
    dictionary = {
        "name": "Short name #" + str(x),
        "description": "Description",
        "external_url": "https://scatter.art/",
        "image": "ipfs://" + cid_hash_image + "/" + str(x) + image_filename,
    }

    with open(f"./{output_folder}/{x}", "w") as outfile:
        json.dump(dictionary, outfile, indent=4)
