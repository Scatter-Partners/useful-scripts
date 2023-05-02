import os

# Define the folder path containing the .json files
folder_path = "json"

# Iterate through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file has a .json extension
    if filename.endswith(".json"):
        # Remove the .json extension from the filename
        new_filename = filename[:-5]
        
        # Create the full file paths for both the original and the renamed files
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {old_file_path} to {new_file_path}")
