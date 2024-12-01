import cv2
from face_recognition import recognize_face
from home_control import control_device

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        user = recognize_face(frame)
        control_device(user)
        cv2.imshow('Face Recognition Home Automation', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
