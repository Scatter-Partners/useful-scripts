# Get snapshots: https://holders.at/

import os

# Set the directory where the snapshots are located
directory = "snapshots"

# Create an empty dictionary to store the lines and their counts
lines_count = dict()

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a .txt file
    if filename.endswith(".txt"):
        # Open the file
        with open(os.path.join(directory, filename)) as file:
            # Read the lines of the file into a set
            lines = file.readlines()
            # Loop through the lines of the file
            for line in lines:
                line = line.strip()
                if line not in lines_count:
                    lines_count[line] = 1
                else:
                    lines_count[line] += 1

# Write the common lines to the output file
with open("output.txt", "w") as file:
    for line, count in lines_count.items():
        if count == len(os.listdir(directory)):
            file.write(line + '\n')