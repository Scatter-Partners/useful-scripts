import sys
import json

# Usage: python generate_json_no_traits.py <cid_hash_image> <output_folder> <image_filename> <supply>

if len(sys.argv) < 5:
    print("Insufficient arguments provided.")
    print("Usage: python generate_json_no_traits.py <cid_hash_image> <output_folder> <image_filename> <supply>")
    sys.exit(1)

cid_hash_image = sys.argv[1]
output_folder = sys.argv[2]
image_filename = sys.argv[3]
supply = int(sys.argv[4])

metadata = []

for x in range(1, supply + 1):
    dictionary = {
        "name": "Short name #" + str(x),
        "description": "Description",
        "external_url": "https://scatter.art/",
        "image": "ipfs://" + cid_hash_image + "/" + str(x) + image_filename,
    }

    metadata.append(dictionary)

# Convert metadata list to JSON and print each JSON object
for data in metadata:
    print(json.dumps(data, indent=4))
