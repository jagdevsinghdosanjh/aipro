
import pyautogui

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            fingers = fingers_up(hand_landmarks)
            if fingers[1] == 1 and fingers[2] == 0:
                pyautogui.click(button='left')
            elif fingers[1] == 0 and fingers[2] == 1:
                pyautogui.click(button='right')
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
