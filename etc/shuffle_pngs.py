import os
import shutil
import random

# Define input and output directories
input_dir = 'input'
output_dir = 'output'

# Check if the output directory exists, if not create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all png files in the input directory
files = [f for f in os.listdir(input_dir) if os.path.splitext(f)[1].lower() == '.png']

# Shuffle the files
random.shuffle(files)

# Copy and rename the files
for i, file in enumerate(files, start=1):
    # Create the new file name
    new_file_name = f'{i}.png'

    # Get the paths
    input_file_path = os.path.join(input_dir, file)
    output_file_path = os.path.join(output_dir, new_file_name)

    # Copy the file
    shutil.copyfile(input_file_path, output_file_path)
