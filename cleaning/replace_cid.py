import os

# Iterate over all files in the current directory
for file in os.listdir():
  # Open the file for reading
  if file == '.DS_Store':  # Skip macOS .DS_Store files
            continue
  with open(file, 'r', encoding="utf-8") as f:
    # Read the contents of the file
    contents = f.read()
  # Replace "REPLACEME" with "REPLACED"
  contents = contents.replace("5,000", "5,000")
  # Open the file for writing
  with open(file, 'w') as f:
    # Write the modified contents to the file
    f.write(contents)
