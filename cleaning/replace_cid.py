import os

# Iterate over all files in the current directory
for file in os.listdir():
  # Open the file for reading
  with open(file, 'r') as f:
    # Read the contents of the file
    contents = f.read()
  # Replace "REPLACEME" with "REPLACED"
  contents = contents.replace("REPLACEME", "REPLACED")
  # Open the file for writing
  with open(file, 'w') as f:
    # Write the modified contents to the file
    f.write(contents)