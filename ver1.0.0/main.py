# main.py
import cv2
from webcam_feed import capture_webcam
from hand_tracking import track_hands
from gesture_recognition import fingers_up
from mouse_control import move_mouse, click_mouse

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frame, results = track_hands(frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                fingers = fingers_up(hand_landmarks)
                if fingers[1] == 1:
                    move_mouse(hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y)
                if fingers[1] == 1 and fingers[2] == 0:
                    click_mouse(button='left')
                elif fingers[1] == 0 and fingers[2] == 1:
                    click_mouse(button='right')
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
