import cv2 # to get the camera working
import numpy as np #
import mediapipe as mp
from tensorflow.keras.models import load_model
from time import sleep
from window_sorting import windows_selection
from pynput.keyboard import Key
# for keystroke data

vKeyData = {
    'okay': 'm',#
    # 'stop': 'w',
    # 'peace': 'F',
    'thumbs up': '[',# is working
    'thumbs down': ']',# is working
    'call me': Key.right,
    'rock': Key.left,
    'live long': '-',
    'fist': Key.media_play_pause,  # is working
    'smile': 's'
}


# for window selection
window_name = "vlc"
detector = windows_selection()
detector.window_find()
pid = detector.find_PID(window_name)

is_first = True

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()


# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''
    if is_first:
        sleep(1)
        detector.setFocus(pid)
        is_first = False

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            classID = np.argmax(prediction)
            className = classNames[classID]
            
    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)
    # to show data
    cv2.putText(frame, "okay: Play/pause", (523,18), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (0, 0, 0), 1, cv2.LINE_AA)
  
    cv2.putText(frame, "stop: S", (523,37), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "Peace: F", (523,56), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
  
    cv2.putText(frame, "thumbs up: [", (523,75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "thumbs down: ]", (523,94), cv2.FONT_HERSHEY_SIMPLEX, 0.43, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "call me: m", (523,113), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "rock: +", (523,132), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "live long: -", (523,151), cv2.FONT_HERSHEY_SIMPLEX, 0.64, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "fist: V", (523,170), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "smile: o", (523,189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, cv2.LINE_AA)

    # end of: to show data
    if className != '':
        try:
            detector.keystrokes(False, [vKeyData[className]])
            sleep(0.45)
        except:
            pass

    # Show the final output
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()