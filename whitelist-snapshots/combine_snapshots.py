# Get snapshots: https://holders.at/

import os

# Set the path to the snapshots folder
folder_path = 'snapshots'

# Initialize an empty list to store the contents of the .txt files
contents = []

# Loop through the files in the snapshots folder
for file in os.listdir(folder_path):
    # Check if the file is a .txt file
    if file.endswith('.txt'):
        # Open the file and read its contents
        with open(os.path.join(folder_path, file), 'r') as f:
            file_contents = f.read()
        # Add the contents of the file to the list
        contents.append(file_contents)

# Combine the contents of the .txt files into a single string
combined_contents = '\n'.join(contents)

# Split the combined contents into a list of lines
lines = combined_contents.split('\n')

# Remove duplicate lines
unique_lines = set(lines)

# Save the unique lines to a new file
with open('output.txt', 'w') as f:
    f.write('\n'.join(unique_lines))
