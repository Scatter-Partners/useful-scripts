import os
import json

def main():
    folder = "jsons"

    # Check if the folder exists
    if not os.path.exists(folder):
        print(f"Folder '{folder}' not found.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder):
        # Check if the file has a .json extension
        #if filename.endswith(".json"):
        # Remove the .json extension to get the name
        name = os.path.splitext(filename)[0]

        # Load the JSON file
        with open(os.path.join(folder, filename), "r") as file:
            data = json.load(file)

        # Check if the name is in both the 'name' and 'image' fields
        if not (name in data.get("name", "") and name in data.get("image", "")):
            print(f"Issue with file: {filename}")

if __name__ == "__main__":
    main()
