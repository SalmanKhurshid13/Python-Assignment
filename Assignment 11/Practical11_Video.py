import cv2

video = cv2.VideoCapture("videos/sample.mp4")

if not video.isOpened():
    print("Video file not found.")
    exit()

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

save = cv2.VideoWriter(
    "outputs/my_video.avi",
    cv2.VideoWriter_fourcc(*"XVID"),
    fps,
    (width, height)
)

print("Video is running...")
print("Press Q to stop.")

while True:

    ok, frame = video.read()

    if not ok:
        break

    cv2.imshow("Video Player", frame)

    save.write(frame)

    key = cv2.waitKey(25)

    if key == ord("q"):
        break

video.release()
save.release()

cv2.destroyAllWindows()

print("Video saved successfully.")