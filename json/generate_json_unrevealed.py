import json

# Usage: python generate_json.py
# Make sure you create an output folder first
# You can edit the values below

cid_hash_image = "REPLACEME" # upload image with https://nft.storage/ then you can link to its cid here

for x in range(1, 354+1):
    dictionary = {
        "name": "Short name #" + str(x),
        "description": "Description ",
        "external_url": "https://scatter.art/",
        "image": "ipfs://" + cid_hash_image + "/filename.png", # if gif or something else change its filename here
    }
    
    with open("./output/" + str(x), "w") as outfile:
        json.dump(dictionary, outfile, indent=4)