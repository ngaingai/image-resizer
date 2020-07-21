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

Example: Resize to width of 512
```
python batch_image_resize.py /my_photos/ 512
```

Example: Resize to height of 512

```
python batch_image_resize.py /my_photos/ 0 512
```

### Prerequisites

Pillow
```
pip install --upgrade Pillow
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
