import cv2

# Read image in grayscale
img = cv2.imread("images/sample.jpg", 0)

# Check image
if img is None:
    print("Image not found!")
else:
    # Apply Canny Edge Detection
    edges = cv2.Canny(img, 100, 200)

    # Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    # Save output
    cv2.imwrite("outputs/canny_edges.jpg", edges)

    print("Canny Edge Detection completed successfully.")

    cv2.waitKey(0)

cv2.destroyAllWindows()