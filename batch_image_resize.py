import os
import shutil
from PIL import Image

RESIZE_HEIGHT = 300

if __name__ == "__main__":
    dir = os.getcwd()
    resized_dir = dir + "_resized"

    #TODO: Check if resized directory exits, if not then prompt to overwrite it
    #if os.path.exists(resized_dir):
    #   overwrite()

    # shutil.copytree(dir, resized_dir)   # Copies entire source directory
    
    im = Image.open("test.jpg")                               # Open the image
    wpercent = (RESIZE_HEIGHT/float(im.size[1]))    # Calculate aspect ratio
    RESIZE_WIDTH = int(im.size[0]*float(wpercent))  # Calculate new width
    im = im.resize((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)  # Resize the image based on new dimensions
    im = im.save("test.jpg")                        # Save the resized image under the same file name

# Check if script is running directly
# if __name__ == "__main__":
#     output_dir = 'resized'
#     dir = os.getcwd()
#     input_dir = 'images'
#     full_input_dir = dir + '/' + input_dir

#     # If output directory doesn't exist, create it
#     if not os.path.exists(os.path.join(dir, output_dir)):
#         os.mkdir(output_dir)

#     try:
#         for file in os.listdir(full_input_dir):     # Iterate through files and resize them
#             resize_image(input_dir, file, output_dir)
#     except OSError: # Error message if input directory doesn't exist
#         print('file not found')

#     def resize_image(input_dir, infile, output_dir="resized", size=(320, 180)):
#         outfile = os.path.splitext(infile)[0] + "_resized"      # Append _resized to the file name
#         extension = os.path.splitext(infile)[1]                 # Get file extension
        
#         try:
#             img = Image.open(input_dir + '/' + infile)              # Pillow 'Image' class opens file
#             img = img.resize((size[0], size[1]), Image.LANCZOS)     # Resize the image and resample with LANCZOS

#             new_file = output_dir + "/" + outfile + extension
#             img.save(new_file)
#         except IOError:
#             print("unable to resize image {}".format(infile))
        
        
#         pass