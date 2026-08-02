import cv2
import numpy as np

pic = cv2.imread("images/sample.jpg")

if pic is None:
    print("Please check the image.")
    exit()

print("Moving image...")

h, w = pic.shape[:2]

# Move image
move = np.float32([
    [1, 0, 80],
    [0, 1, 40]
])

new_pic = cv2.warpAffine(pic, move, (w, h))

cv2.imshow("Original", pic)
cv2.imshow("Shifted Image", new_pic)

cv2.imwrite("outputs/shifted.jpg", new_pic)

print("Done.")

cv2.waitKey(0)
cv2.destroyAllWindows()