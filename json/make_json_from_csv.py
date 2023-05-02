import csv
import os
from datetime import datetime
import json

now = datetime.now()
current_time = now.strftime("%m-%d-%Y-%I-%M-%S-%p")

cid_hash_image = "REPLACE_ME"
name = "Name #"
description = "Your description"
url = "https://scatter.art/"
file_type = ".png"

output_folder = "output_" + current_time
os.mkdir(output_folder)

id = 1
with open('traits.csv') as csv_file:


    csv_reader = csv.reader(csv_file, delimiter=',')
    # Get the keys from the first row
    keys = next(csv_reader) 
    for row in csv_reader:
        dictionary = {
            "name": name + str(id),
            "description": description,
            "external_url": url,
            "image": "ipfs://" + cid_hash_image + "/" + str(id) + file_type,
        }
        dictionary["attributes"] = []    
        # Create an associated array using the keys and the current row
        data = dict(zip(keys, row))
        # Print the contents of each column using the keys
        print(id)
        for key in keys:
            if key != "ID" and key != "" and data[key] and data[key] != "None":
                print(key + ": " + data[key])
                dictionary["attributes"].append({
                    "trait_type": key.strip(),
                    "value": data[key].strip()
                })
        with open("./" + output_folder + "/" + str(id), "w") as outfile:
            json.dump(dictionary, outfile, indent=4)
        id = id + 1