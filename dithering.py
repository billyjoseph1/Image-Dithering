from PIL import Image

def apply_dithering(image):
    # Convert the image to grayscale
    image = image.convert('L')

    width, height = image.size
    for y in range(height):
        for x in range(width):
            old_pixel = image.getpixel((x, y))
            new_pixel = 0 if old_pixel < 128 else 255  # Thresholding

            image.putpixel((x, y), new_pixel)

            # Calculate error
            error = old_pixel - new_pixel

            # Propagate the error to neighboring pixels
            if x < width - 1:
                image.putpixel((x + 1, y), image.getpixel((x + 1, y)) + int(error * 7 / 16))
            if x > 0 and y < height - 1:
                image.putpixel((x - 1, y + 1), image.getpixel((x - 1, y + 1)) + int(error * 3 / 16))
            if y < height - 1:
                image.putpixel((x, y + 1), image.getpixel((x, y + 1)) + int(error * 5 / 16))
            if x < width - 1 and y < height - 1:
                image.putpixel((x + 1, y + 1), image.getpixel((x + 1, y + 1)) + int(error * 1 / 16))

    return image

if __name__ == "__main__":
    # Load an image from the local machine
    image_path = "D:/Pictures/facebook/0_GettyImages-1244643221.jpg"  # Replace with your image path
    original_image = Image.open(image_path)

    # Perform dithering
    dithered_image = apply_dithering(original_image)

    # Display the original and dithered images
    original_image.show()
    dithered_image.show()
