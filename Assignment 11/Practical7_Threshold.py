import cv2

# Read image in grayscale
img = cv2.imread("images/sample.jpg", 0)

# Check image
if img is None:
    print("Image not found!")
else:
    # Apply binary threshold
    ret, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Threshold", threshold)

    # Save output
    cv2.imwrite("outputs/threshold_image.jpg", threshold)

    print("Threshold applied successfully.")

    cv2.waitKey(0)

cv2.destroyAllWindows()