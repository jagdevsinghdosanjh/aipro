# gesture_recognition.py
def fingers_up(hand_landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers
