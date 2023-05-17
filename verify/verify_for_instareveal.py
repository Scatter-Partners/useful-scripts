import os
import json
import hashlib

def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    image_folder = "images"
    json_folder = "json"
    duplicate_images = {}
    valid_json = True
    malformed_json = []
    unique_attributes = {}
    duplicate_attributes = {}
    image_pattern_errors = []
    image_name_errors = []
    missing_image_errors = []
    
    if not os.path.exists(image_folder) or not os.path.exists(json_folder):
        print("Critical Error: 'images' or 'json' folder not found.")
        return

    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    json_files = [f for f in os.listdir(json_folder) if os.path.isfile(os.path.join(json_folder, f))] #and f.endswith('.json')]

    for image_file in image_files:
        file_path = os.path.join(image_folder, image_file)
        file_hash = md5(file_path)
        if file_hash in duplicate_images:
            duplicate_images[file_hash].append(image_file)
        else:
            duplicate_images[file_hash] = [image_file]

    for json_file in json_files:
        file_path = os.path.join(json_folder, json_file)
        if json_file == '.DS_Store':  # Skip macOS .DS_Store files
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                attributes = json_data.get("attributes")
                image = json_data.get("image")

                attributes_str = json.dumps(attributes, sort_keys=True)
                if attributes_str in unique_attributes:
                    if attributes_str in duplicate_attributes:
                        duplicate_attributes[attributes_str].append(json_file)
                    else:
                        duplicate_attributes[attributes_str] = [unique_attributes[attributes_str], json_file]
                else:
                    unique_attributes[attributes_str] = json_file



                if image is not None:
                    expected_image_name = json_file.rsplit(".", 1)[0]
                    
                    _, image_name_with_ext = os.path.split(image)
                    image_name, _ = os.path.splitext(image_name_with_ext)
                    if image_name != expected_image_name:                    
                        image_name_errors.append(json_file)
                    
                    if not image.startswith("ipfs://REPLACEME/"):
                        image_pattern_errors.append(json_file)

                expected_image_exts = ['.png', '.jpg', '.jpeg', '.gif']
                image_found = False
                for ext in expected_image_exts:
                    if f"{expected_image_name}{ext}" in image_files:
                        image_found = True
                        break
                if not image_found:
                    missing_image_errors.append(json_file)

        except json.JSONDecodeError:
            valid_json = False
            malformed_json.append(json_file)

    
    for k, v in duplicate_images.items():
        if len(v) > 1:
            print("Duplicate images:")
            print(", ".join(v))
    if len(duplicate_images) == len(image_files):
        print("No duplicate images found.")

    if valid_json:
        print("All JSON files are valid.")
    else:
        print("Malformed JSON files:", ", ".join(malformed_json))
 
    if len(image_files) == len(json_files):
        print("The number of files in each folder is the same.")
    else:
        print("Error: Different number of files in each folder.")

    if not image_name_errors:
        print("All JSON files have the correct filename in the image field.")
    else:
        print("JSON files with incorrect filename in the image field:", ", ".join(image_name_errors))

    if not missing_image_errors:
        print("All JSON files have a matching image file.")
    else:
        print("JSON files with a missing corresponding image file:", ", ".join(missing_image_errors))
		
    if not duplicate_attributes:
        print("All JSON files have unique attributes.")
    else:
        for k, v in duplicate_attributes.items():
            print("Files with same attributes:", ", ".join(v))

    if not image_pattern_errors:
        print("All JSON files have the correct image pattern.")
    else:
        print("JSON files with incorrect image pattern:", ", ".join(image_pattern_errors))

    if valid_json and not image_name_errors and not duplicate_attributes and not image_pattern_errors and len(image_files) == len(json_files) and not missing_image_errors:
        print("All tests passed.")
    else:
        print("Some tests did not pass.")


main()
