# Batch Image Resizer
<ul>
  <li>Takes a source folder</li>
  <li>Scans through the folder and all sub-folders</li>
  <li>Finds and resizes all images (keeping aspect-ratio) according to desired dimension (width or height)</li>
  <li>Outputs all resized images into new folder with source folder tree intact</li>
</ul>

## Usage

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
Python 3.8.3

Pillow
```
pip install --upgrade Pillow
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
