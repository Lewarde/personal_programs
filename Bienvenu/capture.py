import cv2

def capture_frame(filename="tmp_frame.jpg", camera_index=0):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise RuntimeError("❌ Caméra inaccessible")

    for _ in range(5):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            raise RuntimeError("❌ Erreur de lecture de la caméra")

    cap.release()
    cv2.imwrite(filename, frame)
    return filename
