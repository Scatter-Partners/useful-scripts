import os
import hashlib
from PIL import Image

def get_image_hash(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
        return hashlib.md5(image_data).hexdigest()

def find_duplicate_images(images_folder):
    image_hashes = {}
    duplicate_images = []

    for root, _, files in os.walk(images_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)
                image_hash = get_image_hash(image_path)

                if image_hash in image_hashes:
                    duplicate_images.append((image_path, image_hashes[image_hash]))
                else:
                    image_hashes[image_hash] = image_path

    return duplicate_images

def main():
    images_folder = "images"
    duplicate_images = find_duplicate_images(images_folder)

    if duplicate_images:
        print("Duplicate images found:")
        for duplicate, original in duplicate_images:
            print(f"  {duplicate} is a duplicate of {original}")
    else:
        print("No duplicate images found.")

if __name__ == "__main__":
    main()
