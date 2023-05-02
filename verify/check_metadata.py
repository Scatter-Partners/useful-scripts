import os
import json

# set the path to the directory containing the JSON files
path_to_json_files = "json"

# loop through each file in the directory
for filename in os.listdir(path_to_json_files):
    # check if the file is a JSON file
    #if filename.endswith(".json"):
    # load the file as a JSON object
    with open(os.path.join(path_to_json_files, filename), "r", encoding="utf-8") as f:
        json_data = json.load(f)
    
    # extract the expected number from the filename
    expected_num = filename.split(".")[0]

    # check if the numbers match
    if expected_num not in json_data["name"]:
        # print a message indicating the mismatch
        print(f"Error: Filename {filename} does not match name field in JSON object.")

    # check if the "image" attribute contains the expected number
    if expected_num not in json_data["image"]:
        # print a message indicating the mismatch
        print(f"Error: Filename {filename} expected image number {expected_num}, but found {json_data['image']}")