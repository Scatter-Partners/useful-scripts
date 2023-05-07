import json
import os

# Usage: python generate_json.py
# You must edit the values below to fit your needs
# Verify the output JSON files are how you want them to be

cid_hash_image = "REPLACEME" # upload image with https://nft.storage/ then you can link to its cid here
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'Created folder: "{output_folder}"')

for x in range(1, 354+1):
    dictionary = {
        "name": "Short name #" + str(x),
        "description": "Description ",
        "external_url": "https://scatter.art/",
        "image": "ipfs://" + cid_hash_image + "/filename.png", # if gif or something else change its filename here
    }
    
    with open("./" + output_folder + "/" + str(x), "w") as outfile:
        json.dump(dictionary, outfile, indent=4)
