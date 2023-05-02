import os
import json

input_folder = "json"
output_folder = "output"

for filename in os.listdir(input_folder):
    #if filename.endswith(".json"):
    file_path = os.path.join(input_folder, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
   
    
    # Update JSON fields
    data["name"] = f"Name {i}"
    data["image"] = f"ipfs://REPLACEME/{i}.png"
    data["description"] = "Your description"
    
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
    
    output_file_path = os.path.join(output_folder, filename)
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)