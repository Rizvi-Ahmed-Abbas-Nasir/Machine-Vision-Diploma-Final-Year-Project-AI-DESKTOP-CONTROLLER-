import cv2
import time,  math, numpy as np
import mediapipe as mp
import pyautogui, autopy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import VirtualGloveModule as htm



def  main():
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    # cTime = 0

    face_mash = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    detector = htm.handDetector(maxHands=1, detectionCon=0.85, trackCon=0.8)

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()  # (-63.5, 0.0, 0.5) min max

    minVol = -63
    maxVol = volRange[1]
    print(volRange)
    hmin = 50
    hmax = 200
    volBar = 400
    volPer = 0
    vol = 0
    color = (0, 215, 255)

    tipIds = [4, 8, 12, 16, 20]
    mode = ''
    active = 0

    pyautogui.FAILSAFE = False
    screen_w, screen_h = pyautogui.size()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        print(lmList, "List of Landmarks")
        # print(lmList)
        fingers = []
        # _, frame = cap.read()
        # frame = cv2.flip(frame, 1) this will filp the frame
        rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = face_mash.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = img.shape
        # Below code is for eye detection
        if landmark_points:
            landmarks = landmark_points[0].landmark
            # for landmark in landmarks[]: this will capture the whole face
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                capture = cv2.circle(img, (x, y), 3, (0, 255, 0))
                print(capture)
        #########--
        if len(lmList) != 0:

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0 - 1]][1]:
                if lmList[tipIds[0]][1] >= lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            elif lmList[tipIds[0]][1] < lmList[tipIds[0 - 1]][1]:
                if lmList[tipIds[0]][1] <= lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            print(fingers)
            if (fingers == [0, 0, 0, 0, 0]) & (active == 0):
                mode = 'N'
            elif (fingers == [0, 1, 0, 0, 0] or fingers == [0, 1, 1, 0, 0]) & (active == 0):
                mode = 'Scroll'
                active = 1
            elif (fingers == [1, 1, 0, 0, 0]) & (active == 0):
                mode = 'Volume'
                active = 1
            elif (fingers == [1, 1, 1, 1, 1]) & (active == 0):
                mode = 'Cursor'
                active = 1

        ############# Scroll 👇👇👇👇##############
        if mode == 'Scroll':
            active = 1
            #   print(mode)
            putText(mode)
            cv2.rectangle(img, (200, 410), (245, 460), (255, 255, 255), cv2.FILLED)
            if len(lmList) != 0:
                if fingers == [0, 1, 0, 0, 0]:
                    # print('up')
                    # time.sleep(0.1)
                    putText(mode='U', loc=(200, 455), color=(0, 255, 0))
                    pyautogui.scroll(300)

                if fingers == [0, 1, 1, 0, 0]:
                    # print('down')
                    #  time.sleep(0.1)
                    putText(mode='D', loc=(200, 455), color=(0, 0, 255))
                    pyautogui.scroll(-300)
                elif fingers == [0, 0, 0, 0, 0]:
                    active = 0
                    mode = 'N'
        ################# Volume 👇👇👇####################
        if mode == 'Volume':
            active = 1
            # print(mode)
            putText(mode)
            if len(lmList) != 0:
                if fingers[-1] == 1:
                    active = 0
                    mode = 'N'
                    print(mode)

                else:

                    #   print(lmList[4], lmList[8])
                    x1, y1 = lmList[4][1], lmList[4][2]
                    x2, y2 = lmList[8][1], lmList[8][2]
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    cv2.circle(img, (x1, y1), 10, color, cv2.FILLED)
                    cv2.circle(img, (x2, y2), 10, color, cv2.FILLED)
                    cv2.line(img, (x1, y1), (x2, y2), color, 3)
                    cv2.circle(img, (cx, cy), 8, color, cv2.FILLED)

                    length = math.hypot(x2 - x1, y2 - y1)
                    # print(length)

                    # hand Range 50-300
                    # Volume Range -65 - 0
                    vol = np.interp(length, [hmin, hmax], [minVol, maxVol])
                    volBar = np.interp(vol, [minVol, maxVol], [400, 150])
                    volPer = np.interp(vol, [minVol, maxVol], [0, 100])
                    print(vol)
                    volN = int(vol)
                    if volN % 4 != 0:
                        volN = volN - volN % 4
                        if volN >= 0:
                            volN = 0
                        elif volN <= -64:
                            volN = -64
                        elif vol >= -11:
                            volN = vol

                    #    print(int(length), volN)
                    volume.SetMasterVolumeLevel(vol, None)
                    if length < 50:
                        cv2.circle(img, (cx, cy), 11, (0, 0, 255), cv2.FILLED)

                    cv2.rectangle(img, (30, 150), (55, 400), (209, 206, 0), 3)
                    cv2.rectangle(img, (30, int(volBar)), (55, 400), (215, 255, 127), cv2.FILLED)
                    cv2.putText(img, f'{int(volPer)}%', (25, 430), cv2.FONT_HERSHEY_COMPLEX, 0.9, (209, 206, 0), 3)

        #######################################################################
        if mode == 'Cursor':
            active = 1
            # print(mode)
            putText(mode)
            cv2.rectangle(img, (110, 20), (620, 350), (255, 255, 255), 3)

            if fingers[1:] == [0, 0, 0, 0]:  # thumb excluded
                active = 0
                mode = 'N'
                print(mode)
            else:
                if len(lmList) != 0:
                    x1, y1 = lmList[8][1], lmList[8][2]
                    w, h = autopy.screen.size()
                    X = int(np.interp(x1, [110, 620], [0, w - 1]))
                    Y = int(np.interp(y1, [20, 350], [0, h - 1]))
                    cv2.circle(img, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255),
                               cv2.FILLED)  # First Finger (Color)White
                    cv2.circle(img, (lmList[4][1], lmList[4][2]), 7, (0, 255, 0), cv2.FILLED)  # thumb (Color)Green
                    cv2.circle(img, (lmList[20][1], lmList[20][2]), 7, (0, 255, 0), cv2.FILLED)  # Pinky (Color)Green
                    cv2.circle(img, (lmList[16][1], lmList[16][2]), 7, (0, 255, 0), cv2.FILLED)  # Pinky (Color)Green
                    cv2.circle(img, (lmList[12][1], lmList[12][2]), 7, (0, 255, 0), cv2.FILLED)  # Pinky (Color)Green

                    if X % 2 != 0:
                        X = X - X % 2
                    if Y % 2 != 0:
                        Y = Y - Y % 2
                    print(X, Y)
                    autopy.mouse.move(X, Y)
                    #  pyautogui.moveTo(X,Y)
                    if fingers[0] == 0:
                        cv2.circle(img, (lmList[4][1], lmList[4][2]), 7, (0, 0, 255), cv2.FILLED)  # thumb
                        pyautogui.click()

                    if fingers[4] == 0:
                        cv2.circle(img, (lmList[20][1], lmList[20][2]), 7, (0, 0, 255), cv2.FILLED)  # thumb
                        pyautogui.rightClick()

                    if fingers[2] == 0:
                        cv2.circle(img, (lmList[12][1], lmList[12][2]), 7, (0, 0, 255), cv2.FILLED)  # thumb
                        pyautogui.mouseDown(button="left")
                        pyautogui.moveTo(X, Y, duration=0.1)

                    if fingers[3] == 0:
                        cv2.circle(img, (lmList[16][1], lmList[16][2]), 7, (0, 0, 255), cv2.FILLED)  # thumb
                        pyautogui.doubleClick()

        # cv2.imshow('Eye Controlled Mouse ', frame)
        def putText(mode, loc=(250, 450), color=(0, 255, 255)):
            cv2.putText(img, str(mode), loc, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        3, color, 3)

        cTime = time.time()
        fps = 1 / ((cTime + 0.01) - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS:{int(fps)}', (480, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
        cv2.imshow('Hand LiveFeed', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()