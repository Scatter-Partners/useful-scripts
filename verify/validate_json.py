import os
import json

json_dir = "json"

for file_name in os.listdir(json_dir):
    
    file_path = os.path.join(json_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            json.load(file)
            #print(f"File OK! {file_name}")
        except json.JSONDecodeError as e:
            print(f"Error in file {file_name}: {e}")
