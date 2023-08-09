from PIL import Image
import os

def overlay_images(source_folder, overlay_image_path, output_folder):
    """
    Overlays a transparent image on all images within the specified folder.
    
    :param source_folder: Folder containing images to overlay on.
    :param overlay_image_path: Path to the transparent image to overlay.
    :param output_folder: Folder to save the overlayed images.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the overlay image
    overlay = Image.open(overlay_image_path)

    # Iterate over all files in the source directory
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith('.png'):
            # Construct the full file path
            file_path = os.path.join(source_folder, file_name)

            # Open the source image
            source_image = Image.open(file_path)
            
            # Ensure the overlay is the same size as the source image
            overlay_resized = overlay.resize(source_image.size)
            
            # Composite the images
            combined_image = Image.alpha_composite(source_image.convert("RGBA"), overlay_resized)

            # Save to output directory
            combined_image.save(os.path.join(output_folder, file_name))

if __name__ == '__main__':
    SOURCE_FOLDER = './input/'  # Update with the path to your folder containing the images
    OVERLAY_IMAGE_PATH = './overlay.png'  # Update with the path to your transparent overlay image
    OUTPUT_FOLDER = './output/'  # Update with the path to the folder where you want to save the overlayed images

    overlay_images(SOURCE_FOLDER, OVERLAY_IMAGE_PATH, OUTPUT_FOLDER)