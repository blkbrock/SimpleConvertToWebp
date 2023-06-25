import subprocess
import os

def convert_to_webp(input_image_paths, output_folder, quality=50):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_image_path in input_image_paths:
        if not os.path.exists(input_image_path):
            print(f"The file {input_image_path} does not exist. Check the file path and try again.")
            continue
        
        image_name = os.path.basename(input_image_path)
        image_name_without_ext = os.path.splitext(image_name)[0]
        output_image_path = os.path.join(output_folder, f"{image_name_without_ext}.webp")

        command = f"cwebp -q {quality} {input_image_path} -o {output_image_path}"
        subprocess.run(command, shell=True, check=True)

input_images = ["input image paths" , "", "", "",]
output_folder = "output image path"

convert_to_webp(input_images, output_folder)
