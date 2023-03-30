import cv2
from CVZONE_HandTrackingModule import HandDetector
from time import sleep
import time
import numpy as np
import cvzone
from pynput.keyboard import Controller


def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    cap.set(3, 1210)
    cap.set(4, 500)

    detector = HandDetector(detectionCon=0.8)
    keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
            ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "\n"]]
    finalText = ""

    keyboard = Controller()

    def drawAll(img, buttonList):
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                              20, rt=0)
            cv2.rectangle(img, button.pos, (x + w, y + h), (556,255,0), cv2.FILLED)
            cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        return img

    #
    # def drawAll(img, buttonList):
    #     imgNew = np.zeros_like(img, np.uint8)
    #     for button in buttonList:
    #         x, y = button.pos
    #         cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
    #                           20, rt=0)
    #         cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
    #                       (255, 0, 255), cv2.FILLED)
    #         cv2.putText(imgNew, button.text, (x + 40, y + 60),
    #                     cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
    #
    #     out = img.copy()
    #     alpha = 0.5
    #     mask = imgNew.astype(bool)
    #     print(mask.shape)
    #     out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    #     return out

    class Button():
        def __init__(self, pos, text, size=[85, 85]):
            self.pos = pos
            self.size = size
            self.text = text

    buttonList = []
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bboxInfo = detector.findPosition(img)
        img = drawAll(img, buttonList)

        if lmList:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 10, y - 5), (x + w + 5, y + h + 5), (175, 5, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    l, _, _ = detector.findDistance(8, 12, img, draw=False)
                    print(l)

                    ## when clicked
                    if l < 50:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (556,255,5), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text
                        sleep(0.15)



        cv2.rectangle(img, (50, 350), (1125, 450), (556,255,0), cv2.FILLED)
        cv2.putText(img, finalText, (100, 500),
                    cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        cTime = time.time()
        fps = 1 / ((cTime + 0.01) - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS:{int(fps)}', (1100, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
