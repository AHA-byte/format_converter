import os
from PIL import Image
 
# --- Configuration ---
# Change this variable to your desired format: 'png', 'jpeg', or 'jpg'
output_format = 'png'  # Options: 'png', 'jpeg', 'jpg'
 
# For JPEG/JPG, you can set the quality from 1 (worst) to 95 (best)
jpeg_quality = 95
# --- End Configuration ---
 
 
# Define input and output folders
input_folder = 'input'
output_folder = 'output'
 
# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created directory: {output_folder}")
 
# Process each file in the input folder
 
# Supported input formats: webp, jfif, jpg, jpeg, png, bmp, tiff
supported_extensions = ['.webp', '.jfif', '.jpg', '.jpeg', '.png', '.bmp', '.tiff']
 
for filename in os.listdir(input_folder):
    ext = os.path.splitext(filename)[1].lower()
    if ext in supported_extensions:
        try:
            input_path = os.path.join(input_folder, filename)
            # Open the image
            with Image.open(input_path) as img:
                # Remove the original extension and add the new one
                output_filename = os.path.splitext(filename)[0] + '.' + output_format
                output_path = os.path.join(output_folder, output_filename)
 
                # If saving as JPEG/JPG, it needs to be converted to RGB first
                # to remove any transparency, which JPEG does not support.
                if output_format.lower() in ['jpeg', 'jpg']:
                    # Create a new image with a white background if the original has transparency
                    if img.mode == 'RGBA':
                        # Create a new image with a white background
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.getchannel('A')) # Paste image using alpha channel as mask
                        background.save(output_path, 'jpeg', quality=jpeg_quality)
                    else:
                        # If no transparency, just convert to RGB
                        rgb_img = img.convert('RGB')
                        rgb_img.save(output_path, 'jpeg', quality=jpeg_quality)
                else:
                    # Save as PNG (or other formats), preserving transparency
                    img.save(output_path, output_format.upper())
                print(f"Converted '{filename}' to '{output_filename}'")
 
        except Exception as e:
            print(f"Could not convert {filename}. Reason: {e}")
 
print("\nConversion process finished. ✨")
 