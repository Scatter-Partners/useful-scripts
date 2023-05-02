import json
import os
import hashlib

all_hashes = {}

for filename in os.listdir("output_final_json"):
    #if filename.endswith(".json"):
    with open("output_final_json/" + filename) as json_file:
        json_data = json.load(json_file)

    big_hash = ""
    attributes = json_data["attributes"]
    
    # sort the attributes list by trait_type
    attributes.sort(key=lambda x: x["trait_type"])
    
    for attribute in attributes:
        trait_type = attribute["trait_type"]
        if trait_type != "Name":
            value = attribute["value"]
            value_hash = hashlib.sha256(value.encode()).hexdigest()
            big_hash += value_hash

    final_hash = hashlib.sha256(big_hash.encode()).hexdigest()
    all_hashes[filename] = final_hash

duplicates = {}
for key, value in all_hashes.items():
    if value in duplicates:
        duplicates[value].append(key)
    else:
        duplicates[value] = [key]

for key, value in duplicates.items():
    if len(value) > 1:
        print("Duplicate hash found for files: " + str(value))
