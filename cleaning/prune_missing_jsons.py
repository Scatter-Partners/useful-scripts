import os
import shutil

# Set input and output folder paths
input_folder = "input"
output_folder = "output"

# Check if output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create images and json folders inside output folder if they don't already exist
for folder in ["images", "json"]:
    folder_path = os.path.join(output_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Loop through files in input/images folder and store them in a list
input_images_folder = os.path.join(input_folder, "images")
image_files = [f for f in os.listdir(input_images_folder) if os.path.isfile(os.path.join(input_images_folder, f))]

# Copy each image file from input/images to output/images
for image_file in image_files:
    src = os.path.join(input_images_folder, image_file)
    dst = os.path.join(output_folder, "images", image_file)
    shutil.copy(src, dst)

    # Check for matching JSON files and copy them to output/json
    file_name, file_ext = os.path.splitext(image_file)
    json_file = file_name + ".json"
    json_src = os.path.join(input_folder, "json", json_file)
    if os.path.isfile(json_src):
        json_dst = os.path.join(output_folder, "json", json_file)
        shutil.copy(json_src, json_dst)

print("Prune process complete.")
