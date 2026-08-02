import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    print("Original Size:", img.shape)

    # Resize image
    resized = cv2.resize(img, (500, 400))

    print("Image resized successfully.")

    # Show original image
    cv2.imshow("Original Image", img)

    # Show resized image
    cv2.imshow("Resized Image", resized)

    # Save resized image
    cv2.imwrite("outputs/resized_image.jpg", resized)
    print("Resized image saved.")

    cv2.waitKey(0)

cv2.destroyAllWindows()