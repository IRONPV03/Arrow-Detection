#This was program to make the masking a little better and getting proper
#range for red color.

import cv2
import numpy as np

def empty(img):
    pass

video=cv2.VideoCapture(0)
cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 600, 600)
cv2.createTrackbar('hue_min', "Trackbar", 0, 179, empty)
cv2.createTrackbar('hue_max', "Trackbar", 179, 179, empty)
cv2.createTrackbar('sat_min', "Trackbar", 0, 255, empty)
cv2.createTrackbar('sat_max', "Trackbar", 255, 255, empty)
cv2.createTrackbar('val_min', "Trackbar", 0, 255, empty)
cv2.createTrackbar('val_max', "Trackbar", 255, 255, empty)

while True:
    ret,img=video.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min= cv2.getTrackbarPos('hue_min', 'Trackbar')
    hue_max= cv2.getTrackbarPos('hue_max', 'Trackbar')
    sat_min= cv2.getTrackbarPos('sat_min', 'Trackbar')
    sat_max= cv2.getTrackbarPos('sat_max', 'Trackbar')
    val_min= cv2.getTrackbarPos('val_min', 'Trackbar')
    val_max= cv2.getTrackbarPos('val_max', 'Trackbar')

    lower=np.array([hue_min, sat_min, val_min])
    upper=np.array([hue_max, sat_max, val_max])
    mask=cv2.inRange(hsv, lower, upper)
    cnts,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        area= cv2.contourArea(c)
        if area>500:
            peri=cv2.arcLength(c, True)
            approx=cv2.approxPolyDP(c, 0.01*peri, True)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            if len(approx)==4:
                a,b,w,h=cv2.boundingRect(approx)
                ar=w/h
                if ar==1:
                    cv2.putText(img, 'Square', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
                else:
                    cv2.putText(img, 'Rectangle', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            
            elif len(approx)==3:
                cv2.putText(img, 'Triangle', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            
            elif len(approx) == 5:
                cv2.putText(img, 'Pentagon', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
                          
            elif len(approx) == 6:
                cv2.putText(img, 'Hexagon', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
                              
            elif len(approx) == 7:
                cv2.putText(img, 'Arrow', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
                
            elif len(approx) == 8:
                cv2.putText(img, 'Octagon', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            
            else:
                cv2.putText(img, 'Circle', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
    cv2.imshow('Image', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('Mask', mask)
    k=cv2.waitKey(1)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows()
