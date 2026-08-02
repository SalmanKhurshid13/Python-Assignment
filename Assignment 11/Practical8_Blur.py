import cv2

# Read image
img = cv2.imread("images/sample.jpg")

# Check image
if img is None:
    print("Image not found!")
else:
    # Gaussian Blur
    gaussian = cv2.GaussianBlur(img, (7, 7), 0)

    # Median Blur
    median = cv2.medianBlur(img, 7)

    # Show images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Median Blur", median)

    # Save output images
    cv2.imwrite("outputs/gaussian_blur.jpg", gaussian)
    cv2.imwrite("outputs/median_blur.jpg", median)

    print("Gaussian Blur and Median Blur applied successfully.")

    cv2.waitKey(0)

cv2.destroyAllWindows()