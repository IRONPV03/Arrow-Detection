#This the first final program but issue with this program was masking
#was proper and angle was made with onclick.

import cv2
import numpy as np
import math

points=[]
video=cv2.VideoCapture(0)

angd=0
while True:
    ret,imgx=video.read()
    img=cv2.resize(imgx, (1000,750))
    cv2.line(img, (img.shape[1]//2,0), (img.shape[1]//2,200),(255,0,0), 1)
    #cv2.line(img, (0,img.shape[0]//2), (1000,img.shape[0]//2),(0,255,0), 1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower=np.array([0,100,20])
    upper=np.array([5,255,255])
    mask=cv2.inRange(hsv, lower, upper)
    cnts,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for c in cnts:
        area= cv2.contourArea(c)
        if area>1000:
            peri=cv2.arcLength(c, True)
            approx=cv2.approxPolyDP(c, 0.01*peri, True)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            if len(approx)==4:
                cv2.putText(img, 'Rectangle', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            
            else:
                cv2.putText(img, 'Red arrow', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)


    points=[(img.shape[1]//2,img.shape[0]//2), (750,img.shape[0]//2)]
    def mouse(e, x, y, d, f):
        if e==cv2.EVENT_LBUTTONDOWN:
            points.append([x,y])
            cv2.imshow('Image',img)
            degrees=angle()
    cv2.putText(img, str(angd), (10,700), cv2.FONT_HERSHEY_DUPLEX, 2, (0,0,255), 5)

    def angle():
        global angd
        a=points[0]
        b=points[1]
        c=points[2]
        m1= (a[1]-b[1])/(a[0]-b[0])
        m2= (a[1]-c[1])/(c[0]-a[0])
        angr= math.atan((m2-m1)/1+m1*m2)
        angd=round(math.degrees(angr))
        if c[0]==img.shape[1]//2 and c[1]<img.shape[0]//2:
            angd=0
        elif c[0]>img.shape[1]//2 and c[1]<img.shape[0]//2:
            angd=90-angd
        elif c[0]>img.shape[1]//2 and c[1]==img.shape[0]//2:
            angd=90
        elif c[0]>img.shape[1]//2 and c[1]>img.shape[0]//2:
            angd=90+abs(angd)
        elif c[0]>img.shape[1]//2 and c[1]>img.shape[0]//2:
            angd=180
        elif c[0]<img.shape[1]//2 and c[1]>img.shape[0]//2:
            angd=270-angd
        elif c[0]<img.shape[1]//2 and c[1]==img.shape[0]//2:
            angd=270
        else:
            angd=270+abs(angd)
        return angd
    
    cv2.imshow('Image', img)
    cv2.imshow('Mask', mask)
    cv2.setMouseCallback('Image', mouse)
    k=cv2.waitKey(1)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows()
