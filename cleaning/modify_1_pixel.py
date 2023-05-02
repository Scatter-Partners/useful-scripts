# This modifies images directly make sure you have a backup!

import glob
from PIL import Image

files = []
for file in glob.glob('./images/*'):
    files.append(file)

for file in files:
    if file.endswith(".png"):
        print(file)
        image = Image.open(file)
        rgb_image = image.convert("RGB")
        rgb_pixel_value = rgb_image.getpixel((0, 0))
        print(rgb_pixel_value[0])
        new_rgb = (rgb_pixel_value[0] - 1,
                   rgb_pixel_value[1] - 1, rgb_pixel_value[2] - 1, 255)
        print(new_rgb)
        image.putpixel((0, 0), new_rgb)
        image.save(file)