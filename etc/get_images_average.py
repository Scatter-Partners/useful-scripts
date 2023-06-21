# This script will average together all images in the images folder to create an avg image file

from PIL import Image
import os
import numpy as np

image_filetype = '.png'

def average_images(image_folder):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(image_filetype)]
    image_files.sort()

    avg_img = None
    count = 0

    for image_file in image_files:
        print(f"{image_file}.. ", end="")
        img_path = os.path.join(image_folder, image_file)
        img = Image.open(img_path).convert('RGBA') # Ensure the image is in RGBA format
        img_arr = np.array(img, dtype=np.float64)

        if avg_img is None:
            avg_img = img_arr
        else:
            avg_img = (count * avg_img + img_arr) / (count + 1)

        count += 1

    # Convert averaged image back into an image object
    avg_img = Image.fromarray(np.uint8(avg_img))

    # Save the result
    avg_img.save("avg" + image_filetype)

# Use the function
average_images("images")
