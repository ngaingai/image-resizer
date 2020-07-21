import os
import sys
import shutil
from PIL import Image

def resize_image(source_image, output_path, extension):
    print(source_image)
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.splitext(source_file)[0]                  # Takes filename of source image

    im = Image.open(source_image)                                   # Open the image
    RESIZE_WIDTH = int(sys.argv[2])

    if RESIZE_WIDTH:
        wpercent = (RESIZE_WIDTH/float(im.size[0]))                     # Calculate aspect ratio
        RESIZE_HEIGHT = int(im.size[1]*float(wpercent))                 # Calculate new height        
    else: 
        RESIZE_HEIGHT = int(sys.argv[3])
        wpercent = (RESIZE_HEIGHT/float(im.size[1]))                    # Calculate aspect ratio
        RESIZE_WIDTH = int(im.size[0]*float(wpercent))                  # Calculate new width

    im = im.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)      # Resize the image based on new dimensions

    output_img = output_dir + "/" + output_file + extension
    im.save(output_img)                                                 # Save the resized image under the same file name

if __name__ == "__main__":
    dir = str(sys.argv[1])[:-1]
    
    resized_dir = dir + "_resized"
    converted = 0

    if not os.path.exists(resized_dir):
        os.mkdir(resized_dir)

    for (root, dirs, files) in os.walk(dir, topdown=False):    # Traverse through directory tree
        for source_file in files: 
            extension = os.path.splitext(source_file)[1]
            source_path = os.path.relpath(root + "/" + source_file)
            output_path = resized_dir + "/" + os.path.relpath(root + "/" + source_file, dir)
            if extension == ".png" or extension == ".jpg" or extension == ".gif":
                resize_image(source_path, output_path, extension)
                converted += 1

    print("\nDone! \n" + str(converted) + " images converted\n")