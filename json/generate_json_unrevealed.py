import json
import os

# Usage: python generate_json.py
# Make sure you create an output folder first
# You can edit the values below

cid_hash_image = "REPLACEME"  # upload image with https://nft.storage/ then you can link to its cid here
output_folder = "output"
image_filename = ""  # include this if needed
supply = 1000

if not os.path.exists(output_folder):
  os.makedirs(output_folder)
  print(f'Created folder: "{output_folder}"')

for x in range(1, supply + 1):
  dictionary = {
    "name": "Short name #" + str(x),
    "description": "Description ",
    "external_url": "https://scatter.art/",
    "image": "ipfs://" + cid_hash_image + "/" + image_filename,
  }

  with open("./" + output_folder + "/" + str(x), "w") as outfile:
    json.dump(dictionary, outfile, indent=4)
