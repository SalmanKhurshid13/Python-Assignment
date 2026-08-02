import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape[:2]

    # Find center of image
    center = (cols // 2, rows // 2)

    # Create rotation matrix
    matrix = cv2.getRotationMatrix2D(center, 45, 1)

    # Rotate image
    rotated = cv2.warpAffine(img, matrix, (cols, rows))

    # Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    # Save rotated image
    cv2.imwrite("outputs/rotated_image.jpg", rotated)

    print("Image rotated successfully.")

    cv2.waitKey(0)

cv2.destroyAllWindows()