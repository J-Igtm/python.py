import cv2

print("=== Webcam Access Detector ===")

camera = cv2.VideoCapture(0)

if camera.isOpened():
    print("Webcam detected ✅")
else:
    print("Webcam not found ❌")

camera.release()