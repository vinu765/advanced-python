from PIL import Image, ImageFilter

try:
    # Open an image file
    img = Image.open(r"C:\Users\bhava\Pictures\example.jpg")

    # Display the original image
    img.show()

    # Resize the image to a specific width and height
    resized_img = img.resize((400, 300))
    resized_img.show()

    # Rotate the image by a specific angle (in degrees)
    rotated_img = img.rotate(45)
    rotated_img.show()

    # Apply a Gaussian blur filter to the image
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))
    blurred_img.show()

    # Convert the image to grayscale
    grayscale_img = img.convert("L")
    grayscale_img.show()

    # Save the manipulated image to a file
    grayscale_img.save("example_grayscale.jpg")

except Exception as e:
    print("An error occurred:", e)