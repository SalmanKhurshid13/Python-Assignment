import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Flip horizontally
    horizontal = cv2.flip(img, 1)

    # Flip vertically
    vertical = cv2.flip(img, 0)

    # Flip both horizontally and vertically
    both = cv2.flip(img, -1)

    # Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Horizontal Flip", horizontal)
    cv2.imshow("Vertical Flip", vertical)
    cv2.imshow("Both Flip", both)

    # Save images
    cv2.imwrite("outputs/horizontal_flip.jpg", horizontal)
    cv2.imwrite("outputs/vertical_flip.jpg", vertical)
    cv2.imwrite("outputs/both_flip.jpg", both)

    print("All flipped images saved successfully.")

    cv2.waitKey(0)

cv2.destroyAllWindows()