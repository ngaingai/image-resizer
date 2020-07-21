# Batch Image Resizer

Takes a source folder
Scans through the folder and all sub-folders
Finds and resizes all images (keeping aspect-ratio) according to desired dimension
Outputs all resized images into new folder with source folder tree intact

## Getting Started

From terminal:

```
python batch_image_resize.py [/source_directory/] [resize_width] [resize_height]
```

Important: Input '0' for resize_width if you want to resize according to height

Example:
python batch_image_resize.py /my_photos/ 0 512

Will resize all images to a height of 512.

### Prerequisites

Pillow
```
pip install --upgrade Pillow
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
