import os
import shutil

# Create the "output" folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Loop through all the .png files in the "input" folder
i = 1
for filename in os.listdir("input"):
    if filename.lower().endswith(".png"):
        # Construct the new filename as a zero-padded number
        new_filename = f"{i}.png"
        # Copy the file to the "output" folder with the new filename
        shutil.copy(os.path.join("input", filename), os.path.join("output", new_filename))
        i += 1
