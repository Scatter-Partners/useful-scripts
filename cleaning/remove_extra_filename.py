import os
import re
import shutil

input_folder = "input"
output_folder = "output"

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    # Extract the first number from the file name
    match = re.match(r"(\d+).*", filename)
    if match:
        new_filename = f"{match.group(1)}.png"
        old_path = os.path.join(input_folder, filename)
        new_path = os.path.join(output_folder, new_filename)
        # Copy the file and rename it
        shutil.copy2(old_path, new_path)
