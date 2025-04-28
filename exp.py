import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
mp_draw=mp.solutions.drawing_utils
tip_ids=[4, 8, 12, 16, 20]

def get_finger_states(hand_landmarks):
    fingers=[]
    if hand_landmarks.landmark[tip_ids[0]].x<hand_landmarks.landmark[tip_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for i in range(1,5):
        if hand_landmarks.landmark[tip_ids[i]].y<hand_landmarks.landmark[tip_ids[i]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

def get_hand_horizontal_position(hand_landmarks, width):
    avg_x=(hand_landmarks.landmark[0].x + hand_landmarks.landmark[5].x) / 2
    x_pos=int(avg_x*width)
    if x_pos<width*0.33:
        return "left"
    elif x_pos>width*0.66:
        return "right"
    else:
        return "center"

def get_hand_vertical_position(hand_landmarks,height):
    avg_y=(hand_landmarks.landmark[0].y+hand_landmarks.landmark[9].y)/2
    y_pos=int(avg_y*height)
    if y_pos<height*0.4:
        return "up"
    elif y_pos>height*0.6:
        return "down"
    else:
        return "center"

def simulate_key_press(key):
    pyautogui.press(key)
    time.sleep(0)

cap=cv2.VideoCapture(0)
last_action_time=time.time()

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture_text = ""

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        h, w, _ = img.shape
        x_min, y_min = w, h
        x_max, y_max = 0, 0
        for lm in hand_landmarks.landmark:
            x, y = int(lm.x * w), int(lm.y * h)
            x_min=min(x_min, x)
            y_min=min(y_min, y)
            x_max=max(x_max, x)
            y_max=max(y_max, y)
        cv2.rectangle(img, (x_min - 20, y_min - 20), (x_max + 20, y_max + 20), (0, 255, 0), 2)

        fingers = get_finger_states(hand_landmarks)
        hand_position = get_hand_horizontal_position(hand_landmarks, w)
        hand_vertical_position = get_hand_vertical_position(hand_landmarks, h)

        # Slide Left
        # if fingers == [0, 1, 1, 1, 0] and time.time() - last_action_time > 1:
        #     gesture_text = " Slide Left"
        #     simulate_key_press('j')
        #     last_action_time = time.time()

        # # Slide Right
        # elif fingers == [0, 1, 1, 1, 1] and time.time() - last_action_time > 1:
        #     gesture_text = " Slide Right"
        #     simulate_key_press('l')
        #     last_action_time = time.time()

        # # Jump
        # el
        if fingers == [0, 1, 0, 0, 0] and time.time() - last_action_time > 1:
            gesture_text = "Jump"
            simulate_key_press('w')
            last_action_time = time.time()
        # Slide Down
        elif fingers == [1, 1, 1, 1, 1] and time.time() - last_action_time > 1:
            gesture_text = "Slide Down"
            simulate_key_press('s')
            last_action_time = time.time()
        # Turn Right
        elif fingers == [1, 0, 0, 0, 1] and time.time() - last_action_time > 1:
            gesture_text = "Turn Right"
            simulate_key_press('d')
            last_action_time = time.time()
        # Turn Left
        elif fingers == [0, 1, 1, 0, 0] and time.time() - last_action_time > 1:
            gesture_text = "Turn Left"
            simulate_key_press('a')
            last_action_time = time.time()
        # Showing gesture
        if gesture_text:
          cv2.putText(img, gesture_text, (x_min, y_min - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Temple Run Hand Control", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
