import os
import shutil
from PIL import Image

RESIZE_HEIGHT = 380

def resize_image(source_image, output_path, extension):
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.splitext(source_file)[0]                  # Takes filename of source image

    im = Image.open(source_image)                                   # Open the image
    wpercent = (RESIZE_HEIGHT/float(im.size[1]))                    # Calculate aspect ratio
    RESIZE_WIDTH = int(im.size[0]*float(wpercent))                  # Calculate new width
    im = im.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)  # Resize the image based on new dimensions

    output_img = output_dir + "/" + output_file + extension
    im.save(output_img)                                             # Save the resized image under the same file name

    print(source_image)

if __name__ == "__main__":
    dir = os.getcwd()
    resized_dir = dir + "_resized"
    if not os.path.exists(resized_dir):
        os.mkdir(resized_dir)
    converted = 0

    for (root, dirs, files) in os.walk(dir, topdown=False):    # Traverse through directory tree
        for source_file in files: 
            extension = os.path.splitext(source_file)[1]
            source_path = os.path.relpath(root + "/" + source_file, dir)
            output_path = resized_dir + "/" + source_path
            if extension == ".png" or extension == ".jpg" or extension == ".gif":
                resize_image(source_path, output_path, extension)
                converted += 1

    print("\nDone. \n" + str(converted) + " images converted\n")