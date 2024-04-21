import os
import hashlib
from collections import defaultdict

def md5_hash(filepath):
    """Compute the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(directory):
    """Find and print duplicate files in a directory based on MD5 hash."""
    hashes = defaultdict(list)
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = md5_hash(filepath)
            hashes[file_hash].append(filepath)

    # Check for duplicate hashes and print them
    for paths in hashes.values():
        if len(paths) > 1:
            print("Duplicates found:")
            for path in paths:
                print(path)

# Path to the input folder
input_directory = "input"
find_duplicates(input_directory)
