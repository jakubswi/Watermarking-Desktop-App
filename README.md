# Watermarking Application

This Python application allows you to easily watermark images using a graphical user interface (GUI). You can select
both the image you want to watermark and the watermark image itself. The position, size, and transparency of the
watermark can also be adjusted to suit your preferences.

## Requirements

- Python 3.x
- Tkinter library
- Pillow (PIL) library

## Installation

1. Ensure you have Python installed on your system.
2. Install required libraries by running:

    ```bash
   pip install pillow

## Usage

1. Run the script using Python:

    ```bash
   python watermark_app.py

2. Click on the "Browse Files for image" button to select the image you want to watermark.
3. Click on the "Browse Files for watermark" button to select the watermark image.
4. Choose the desired position for the watermark by selecting one of the radio buttons.
5. Adjust the transparency and size of the watermark using the sliders.
6. Click the "Render image" button to apply the watermark to the selected image.
7. The watermarked image will be saved as "watermarked_image.png" in the same directory.

## Note

- Supported image formats for both the main image and watermark are `.jpg`, `.png`, and `.jpeg`.
- Ensure that the watermark image has transparent parts if you intend to use transparency settings.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or
create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
