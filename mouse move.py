import cv2
import numpy as np
from pynput.mouse import Controller, Button

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("1", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("2", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("3", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("4", "Trackbar", 179, 179, nothing)
cv2.createTrackbar("5", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("6", "Trackbar", 255, 255, nothing)

cap= cv2.VideoCapture(0)
mouse= Controller()

resolucao= np.array((1366, 768))

while True:
    _, frame= cap.read()

    imagem= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l1= cv2.getTrackbarPos("1", "Trackbar")
    l2= cv2.getTrackbarPos("2", "Trackbar")
    l3= cv2.getTrackbarPos("3", "Trackbar")
    l4= cv2.getTrackbarPos("4", "Trackbar")
    l5= cv2.getTrackbarPos("5", "Trackbar")
    l6= cv2.getTrackbarPos("6", "Trackbar")

    down= np.array([103, 95, 44])
    upper= np.array([144, 255, 255])

    mascara= cv2.inRange(imagem, down, upper)
    mascara= cv2.erode(mascara, np.ones((5, 5), np.uint8))

    _, contours,_= cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area= cv2.contourArea(cnt)
        aproximacao= cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        
        x= aproximacao.ravel()[0]
        y= aproximacao.ravel()[1]

        if area> 500:
            x= int((1366/640)*x)
            y= int((768/360)*y)
            mouse.position= (x, y)    
            cv2.drawContours(frame, [aproximacao], 0, (0, 0, 0), 5)    
        
    
    cv2.imshow("imagem", frame)

    key= cv2.waitKey(1)
    if key== 27:
        break
    
cap.release()
cv2.destroyAllWindows()

#mouse.position= (x, y)
