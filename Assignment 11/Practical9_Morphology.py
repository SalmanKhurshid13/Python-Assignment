import cv2
import numpy as np

gray = cv2.imread("images/sample.jpg", 0)

if gray is None:
    print("Image not loaded")
    exit()

print("Applying morphology...")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

top = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
black = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", gray)
cv2.imshow("Top Hat", top)
cv2.imshow("Black Hat", black)

cv2.imwrite("outputs/top_hat_result.jpg", top)
cv2.imwrite("outputs/black_hat_result.jpg", black)

print("Operation completed.")

cv2.waitKey(0)
cv2.destroyAllWindows()