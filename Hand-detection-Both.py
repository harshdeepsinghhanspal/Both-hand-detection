import cv2
from cvzone.HandTrackingModule import HandDetector
#use version 1.5.0 for cvzone
#mediapipe version 8.7.1, recommended

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow('Result', img)
    cv2.waitKey(1)