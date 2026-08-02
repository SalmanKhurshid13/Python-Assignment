import cv2

print("OpenCV Practical 1")

image = cv2.imread("images/sample.jpg")

if image is None:
    print("Could not open the image.")
    quit()

print("Image loaded.")

cv2.imshow("My Image", image)

cv2.imwrite("outputs/my_saved_image.jpg", image)

print("Image saved.")

cv2.waitKey(0)

cv2.destroyAllWindows()