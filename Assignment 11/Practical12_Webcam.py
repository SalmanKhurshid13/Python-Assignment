import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Check webcam
if not cap.isOpened():
    print("Error: Cannot access webcam.")
else:
    print("Webcam started successfully.")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Show webcam
        cv2.imshow("Live Webcam", frame)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Webcam closed.")