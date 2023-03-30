import cv2
import numpy as np
import pickle

def main():
    fps = 30
    window_width = 1280
    window_height = 720

    w = 1280
    h = 720
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
    cam.set(cv2.CAP_PROP_FPS, fps)

    class HandsLM():
        import mediapipe as mp
        def __init__(self):
            self.hands = self.mp.solutions.hands.Hands(False, 1, 1, .5, .5)

        def HandData(self, frame):
            landmarks = []
            label = []
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frameRGB)
            if results.multi_hand_landmarks != None:
                for i in results.multi_handedness:
                    for j in i.classification:
                        label.append(j.label)
                for handlandmarks in results.multi_hand_landmarks:
                    Landmarks = []
                    for landmark in handlandmarks.landmark:
                        Landmarks.append((int(w * landmark.x), int(h * landmark.y)))
                    landmarks.append(Landmarks)
            return landmarks, label

    def handLmDist(handData):
        palmsize = (((handData[9][0] - handData[0][0]) ** 2) + (handData[9][1] - handData[0][1]) ** 2) ** (1. / 2.)
        handDistMatx = np.zeros([len(handData), len(handData)], dtype='float')
        for row in range(0, len(handData)):
            for column in range(0, len(handData)):
                handDistMatx[row][column] = ((((handData[row][0] - handData[column][0]) ** 2) + (
                            handData[row][1] - handData[column][1]) ** 2) ** (1. / 2.)) / palmsize
        return handDistMatx

    def errors(unknow_distance, known_distance, keypoints):
        error = 0
        for row in keypoints:
            for column in keypoints:
                error += abs(known_distance[row][column] - unknow_distance[row][column])
        return error

    def GesturesErr(unknown_gesture, Known_gestures, keypoints, gestures_names, tol):
        gestures_Err = []
        for i in range(0, len(gestures_names)):
            gesture_Err = errors(unknown_gesture, Known_gestures[i], keypoints)
            gestures_Err.append(gesture_Err)
        min_err = gestures_Err[0]
        idx = 0
        for i in range(0, len(gestures_Err)):
            if gestures_Err[i] < min_err:
                min_err = gestures_Err[i]
                idx = i
        if min_err < tol:
            return gesture_names[idx]
        if min_err >= tol:
            return 'Unknown'

    with open('AI_KEYBOARD.pkl', 'rb') as f:
        Known_gestures = pickle.load(f)
        gesture_names = pickle.load(f)

    HandsLM = HandsLM()
    keypoints = [0, 4, 5, 8, 9, 12, 13, 16, 17, 20]
    tol = 10
    points = [8, 12]
    target = (0, 0)

    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    alph1 = ['~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'back']

    R1x1 = 225
    R1x2 = 275
    R1y1 = 10  # 400
    R1y2 = 60  # 450
    t1x = 232
    t1y = 55  # 445

    alph2 = ['tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '|']
    R2x1 = 240 + 60
    R2x2 = 290 + 60
    R2y1 = R1y1 + 55
    R2y2 = R1y2 + 55
    t2x = 247 + 60
    t2y = t1y + 50

    alph3 = ['caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'enter']
    R3x1 = 240 + 80
    R3x2 = 290 + 80
    R3y1 = R2y1 + 55
    R3y2 = R2y2 + 55
    t3x = 247 + 80
    t3y = t2y + 50

    alph4 = ['shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?', 'shift']
    R4x1 = 240 + 110
    R4x2 = 290 + 110
    R4y1 = R3y1 + 55
    R4y2 = R3y2 + 55
    t4x = 247 + 110
    t4y = t3y + 55

    alph5 = [' ', 'ctrl', 'fn', ' ', 'alt', 'alt', '', 'ctrl', '']
    R5x1 = 240 + 220
    R5x2 = 240 + 220 + 330 + 50
    R5y1 = R4y1 + 55
    R5y2 = R4y2 + 55
    t5x = 247 + 220 + 330
    t5y = t4y + 55

    select_mode = False

    a = ''
    b = ''
    text = []
    sent = ''

    while True:
        ignore, frame = cam.read()
        frame = cv2.resize(frame, (1280, 720))

        hand_landmarks, hand_label = HandsLM.HandData(frame)

        if hand_landmarks != []:
            unknown_gestures = handLmDist(hand_landmarks[0])
            error = GesturesErr(unknown_gestures, Known_gestures, keypoints, gesture_names, tol)
            # cv2.putText(frame,'Testing Mode:   '+error,(100,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            if error == 'select':
                select_mode = True
            else:
                select_mode = False

        for hand_landmark in hand_landmarks:
            for i in points:
                cv2.circle(frame, hand_landmark[i], 15, (0, 255, 0), 3)
            target = hand_landmark[8]

        for i in range(0, len(alph1), 1):
            if i < len(alph1) - 1:
                x1 = R1x1
                y1 = R1y1
                x2 = R1x2
                y2 = R1y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph1[i], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph1[i], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph1[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph1[i], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b
                            # print(text)

                R1x1 += 5
                R1x2 += 5
                R1x1 += 50
                R1x2 += 50
                t1x = R1x1 + 7

            if i >= len(alph1) - 1:
                x1 = R1x1
                y1 = R1y1
                x2 = R1x1 + 100
                y2 = R1y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph1[-1], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph1[-1], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = ''
                            if b != a:
                                text.remove(text[-1])
                                sent = sent.replace(sent[-1], '')
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph1[i], (t1x, t1y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

        R1x1 = 225
        R1x2 = 275
        t1x = 232

        for i in range(0, len(alph2), 1):
            if i > 0 and i < len(alph2) - 1:
                x1 = R2x1
                y1 = R2y1
                x2 = R2x2
                y2 = R2y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph2[i], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph2[i], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph2[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph2[i], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

                R2x1 += 5
                R2x2 += 5
                R2x1 += 50
                R2x2 += 50
                t2x = R2x1 + 7
            if i >= len(alph2) - 1:
                x1 = R2x1
                y1 = R2y1
                x2 = R2x1 + 80
                y2 = R2y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph2[-1], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph2[-1], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph2[-1]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph2[-1], (t2x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

            if i == 0:
                x1 = R1x1
                y1 = R2y1
                x2 = R1x1 + 70
                y2 = R2y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph2[i], (t1x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph2[i], (t1x, t2y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph2[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph2[i],(t1x,t2y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

        R2x1 = 240 + 60
        R2x2 = 290 + 60
        t2x = 247 + 60

        for i in range(0, len(alph3), 1):
            if i > 0 and i < len(alph3) - 1:
                x1 = R3x1
                y1 = R3y1
                x2 = R3x2
                y2 = R3y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph3[i], (t3x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph3[i], (t3x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph3[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph3[i], (t3x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

                R3x1 += 5
                R3x2 += 5
                R3x1 += 50
                R3x2 += 50
                t3x = R3x1 + 7
            if i >= len(alph3) - 1:
                x1 = R3x1
                y1 = R3y1
                x2 = R3x1 + 115
                y2 = R3y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph3[-1], (t3x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph3[-1], (t3x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph3[-1]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph3[-1],(t3x,t3y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

            if i == 0:
                x1 = R1x1
                y1 = R3y1
                x2 = R1x1 + 90
                y2 = R3y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph3[i], (t1x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph3[i], (t1x, t3y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph3[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph3[i],(t1x,t3y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

        R3x1 = 240 + 80
        R3x2 = 290 + 80
        t3x = 247 + 80

        for i in range(0, len(alph4), 1):
            if i > 0 and i < len(alph4) - 1:
                x1 = R4x1
                y1 = R4y1
                x2 = R4x2
                y2 = R4y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph4[i], (t4x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph4[i], (t4x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph4[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph4[i], (t4x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

                R4x1 += 5
                R4x2 += 5
                R4x1 += 50
                R4x2 += 50
                t4x = R4x1 + 7
            if i >= len(alph4) - 1:
                x1 = R4x1
                y1 = R4y1
                x2 = R4x1 + 140
                y2 = R4y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph4[-1], (t4x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph4[-1], (t4x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph4[-1]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph4[-1],(t4x,t4y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

            if i == 0:
                x1 = R1x1
                y1 = R4y1
                x2 = R1x1 + 120
                y2 = R4y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph4[i], (t1x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph4[i], (t1x, t4y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph4[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph4[i],(t1x,t4y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

        R4x1 = 240 + 110
        R4x2 = 290 + 110
        t4x = 247 + 110

        R1x1 = 225 + 70
        R1x2 = 275 + 70
        t1x = 232 + 70
        for i in range(0, len(alph5), 1):
            if i > 1 and i < 5:
                x1 = R1x1
                y1 = R5y1
                x2 = R1x2
                y2 = R5y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph5[i], (t1x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph5[i], (t1x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph5[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph5[i],(t1x,t5y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

                R1x1 += 5
                R1x2 += 5
                R1x1 += 50
                R1x2 += 50
                t1x = R1x1 + 7
            if i >= 5 and i < len(alph5) - 2:
                x1 = R5x1
                y1 = R5y1
                x2 = R5x2
                y2 = R5y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if i > 5 and i < len(alph5) - 2:
                    if select_mode:
                        if target[1] < y2 and target[1] > y1:
                            if target[0] >= x1 and target[0] <= x2:
                                b = alph5[i]
                                if b != a:
                                    text.append(b)
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                                cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                                            2)
                                a = b

                R5x1 += 5
                R5x2 += 5
                R5x1 += 50
                R5x2 += 50
                t5x = R5x1 + 7
            if i == 0:
                x1 = R5x1
                y1 = R5y1
                x2 = R5x1 + 325
                y2 = R5y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph5[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), -1)
                            cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            a = b

                R5x1 = R5x1 + 330
            if i == 1:
                x1 = R1x1 - 70
                y1 = R5y1
                x2 = R1x1 - 5
                y2 = R5y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph5[i], (t1x - 70, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph5[i], (t1x - 70, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph5[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph5[i],(t1x - 70,t5y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

            if i >= len(alph5) - 2:
                x1 = R5x1
                y1 = R5y1
                x2 = R5x2 + 15
                y2 = R5y2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
                cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                if target[1] < y2 and target[1] > y1:
                    if target[0] >= x1 and target[0] <= x2:
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)
                        cv2.putText(frame, alph5[i], (t5x, t5y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                """if select_mode:
                    if target[1] < y2 and target[1] > y1:
                        if target[0] >= x1 and target[0] <= x2:
                            b = alph5[i]
                            if b != a:
                                text.append(b)
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
                            cv2.putText(frame,alph5[i],(t5x,t5y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                            a = b"""

                R5x1 += 5
                R5x2 += 5
                R5x1 += 65
                R5x2 += 70
                t5x = R5x1 + 7
        R1x1 = 225
        R1x2 = 275
        t1x = 232
        R5x1 = 240 + 220
        R5x2 = 240 + 220 + 330 + 50
        t5x = 247 + 220 + 330

        target = (0, 0)

        if len(sent) < len(text):
            sent += text[-1]
        # print('sent', sent)
        # print('len',len(sent),len(text))

        cv2.rectangle(frame, (10, 560), (1270, 610), (255, 255, 255), -1)
        if len(sent) != 0:
            cv2.putText(frame, sent, (10, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        cv2.imshow('Asquare', frame)


        if cv2.waitKey(1) & 0xff == ord('q'):
            cv2.destroyAllWindows()
            break

    cam.release()



if __name__ == "__main__":
    main()