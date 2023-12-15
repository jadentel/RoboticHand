import cvzone
import cv2
import serial

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(detectionCon=0.7, maxHands=2)
mySerial = cvzone.SerialObject("COM6", 9600, 1)

while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    if lmlist:
        fingers = detector.fingersUp()
        print(fingers)
        mySerial.sendData(fingers)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)