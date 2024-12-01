import pyautogui

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            fingers = fingers_up(hand_landmarks)
            if fingers[1] == 1:
                pyautogui.moveTo(hand_landmarks.landmark[8].x * screen_width, hand_landmarks.landmark[8].y * screen_height)
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
