#This is my final project

import cv2 
import numpy as np
import math

cap = cv2.VideoCapture(0)

while True:
  
    ret, imgx= cap.read()
    frame=cv2.resize(imgx, (1000,750))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    kernel = np.ones((7,7), np.uint8) 
    lower_red = np.array([0,100,20])
    upper_red = np.array([5,255,255])
    l1= np.array([160,100,20])
    u1= np.array([179,255,255])
    mask1= cv2.inRange(hsv, lower_red, upper_red)
    mask2= cv2.inRange(hsv, l1,u1)
    mask= mask1+ mask2
    img_erosion = cv2.erode(mask, kernel)
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    edges = cv2.Canny(res,100,200)
    cnts,_=cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        area= cv2.contourArea(c)
        if area>1500:
            peri=cv2.arcLength(c, True)
            approx=cv2.approxPolyDP(c, 0.01*peri, True)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            if len(approx)==7:
                cv2.putText(frame, 'Red arrow', (x,y), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 5)
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            center = (int(rect[0][0]),int(rect[0][1])) 
            width = int(rect[1][0])
            height = int(rect[1][1])
            angle = int(rect[2])
            if width < height:
                angle =angle
            else:
                angle = 90+angle
         
            label = "Angle " + str(angle) + " degrees"
            cv2.putText(frame, label, (center[0]-50, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, cv2.LINE_AA)
    cv2.imshow('Original',frame)
    cv2.imshow('Edges',img_erosion)
    k = cv2.waitKey(1)
    if k == ord('d'):
        break
  
cap.release()
cv2.destroyAllWindows() 



