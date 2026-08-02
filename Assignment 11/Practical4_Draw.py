import cv2

photo = cv2.imread("images/sample.jpg")

if photo is None:
    print("Image is missing.")
    exit()

print("Drawing on image...")

# Draw a red line
cv2.line(photo, (30, 30), (250, 30), (0, 0, 255), 2)

# Draw a green rectangle
cv2.rectangle(photo, (50, 60), (220, 180), (0, 255, 0), 2)

# Draw a blue circle
cv2.circle(photo, (320, 140), 50, (255, 0, 0), 2)

# Write text
cv2.putText(
    photo,
    "My OpenCV Practice",
    (30, 250),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2,
)

cv2.imshow("Drawing Practice", photo)

cv2.imwrite("outputs/practical4_result.jpg", photo)

print("Finished.")

cv2.waitKey(0)
cv2.destroyAllWindows()