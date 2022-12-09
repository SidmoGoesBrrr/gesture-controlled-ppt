import time

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import cvzone

#camera setup
width, height = 1280, 720
gesture_threshold = 300
fpsReader = cvzone.FPS()
import pyautogui
cap = cv2.VideoCapture(1)
cap.set(3,width)
cap.set(4,height)

#hand detector setup

detector = HandDetector(detectionCon=0.8,maxHands=1)
while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    fps, img = fpsReader.update(img, pos=(1150, 40), color=(0, 255, 0), scale=2, thickness=2)
    #displaying the fps
    hands,img= detector.findHands(img,flipType=False)
    cv2.line(img,(0,gesture_threshold),(width,gesture_threshold),(0,255,0),10)
     #detecting hands and drawing a line to define a threshold

    if hands:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        #detecting fingers and declaring them in an array to check which one is up
        cx,cy=hand["center"]
        hand_type=hand["type"]

        print(fingers)
        if cy<=gesture_threshold:
            time.sleep(1)
            if fingers==[0,0,0,0,0]:
                if hand_type=="Right":
                    cv2.putText(img, "Left", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    #click the left arrow button using pyautogui

                    pyautogui.press('left')
                    
                elif hand_type=="Left":
                    cv2.putText(img, "Right", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    #click the right arrow button using pyautogui
                    pyautogui.press('right')

            elif fingers==[1,0,0,0,1]:
                cv2.putText(img, "Stop", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                pyautogui.press('escape')

            elif fingers==[1,0,0,0,0]:
                cv2.putText(img, "White Screen", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                pyautogui.press('w')

            
    cv2.imshow("image", img)

    key = cv2.waitKey(1)

    if key== ord('q'):
        break
