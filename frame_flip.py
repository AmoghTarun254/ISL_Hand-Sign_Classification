import cv2
import os

# Path to the main directory containing multiple folders of images
input_dir = r'E:\Batch 1(3-9 March)\Day 2'

# Path to save the flipped images
output_dir = r'E:\Flipped Batch 1(3-9 March)\Day 2'
os.makedirs(output_dir, exist_ok=True)

# Loop over each folder inside the main directory
for folder_name in os.listdir(input_dir):
    folder_path = os.path.join(input_dir, folder_name)
    print("Processing folder: ", folder_path)

    # Skip if not a folder
    if not os.path.isdir(folder_path):
        continue

    # Create corresponding folder in the output directory
    output_folder_path = os.path.join(output_dir, folder_name)
    os.makedirs(output_folder_path, exist_ok=True)

    # Loop over each image in the folder
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        # Check for supported image formats
        if not image_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')):
            print(f"Skipping unsupported file: {image_path}")
            continue

        # Read the image
        print("Reading the image")
        image = cv2.imread(image_path)

        # Check if the image was loaded properly
        if image is None:
            print(f"Error loading image: {image_path}")
            continue

        # Flip the image horizontally
        print("Flipping the image")
        flipped_image = cv2.flip(image, 1)

        # Save the flipped image to the output directory
        print("Saving the image")
        output_image_path = os.path.join(output_folder_path, image_name)
        cv2.imwrite(output_image_path, flipped_image)

print("✅ All images have been flipped and saved!")
