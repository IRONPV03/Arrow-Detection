#This made erosion working easy but angle can't be found be
#automatically.

import cv2
import numpy as np
import math

points=[]
video=cv2.VideoCapture(0)

while True:
    ret,imgx=video.read()
    img=cv2.resize(imgx, (1000,750))
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    kernel= np.ones((7,7), np.uint8)
    
    img_erosion = cv2.erode(mask, kernel)
    lower=np.array([0,100,20])
    upper=np.array([5,255,255])
    mask=cv2.inRange(hsv, lower, upper)
    cnts,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts:
        area= cv2.contourArea(c)
        if area>img.shape[1]//2:
            peri=cv2.arcLength(c, True)
            approx=cv2.approxPolyDP(c, 0.01*peri, True)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            if len(approx)==4:
                cv2.putText(img, 'Red quadilateral', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            else:
                cv2.putText(img, 'Red arrow', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)

    points=[(img.shape[1]//2,img.shape[0]//2), (750,img.shape[0]//2)]
    def mouse(e, x, y, d, f):
        if e==cv2.EVENT_LBUTTONDOWN:
            points.append([x,y])
            cv2.imshow('Image',img)
            a=points[0]
            b=points[1]
            c=points[2]
            m1= (a[1]-b[1])/(a[0]-b[0])
            m2= (a[1]-c[1])/(c[0]-a[0])
            angr= math.atan((m2-m1)/1+m1*m2)
            angd=round(math.degrees(angr))
            if c[0]==img.shape[1]//2 and c[1]<img.shape[0]//2:
                angd=0
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]>img.shape[1]//2 and c[1]<img.shape[0]//2:
                angd=90-angd
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]>img.shape[1]//2 and c[1]==img.shape[0]//2:
                angd=90
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]>img.shape[1]//2 and c[1]>img.shape[0]//2:
                angd=90+abs(angd)
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]>img.shape[1]//2 and c[1]>img.shape[0]//2:
                angd=180
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]<img.shape[1]//2 and c[1]>img.shape[0]//2:
                angd=270-angd
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            elif c[0]<img.shape[1]//2 and c[1]==img.shape[0]//2:
                angd=270
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            else:
                angd=270+abs(angd)
                cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
            print(angd)
            cv2.putText(img, str(angd), (c[0],c[1]), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
    cv2.imshow('Image', img)
    cv2.imshow('Mask', img_erosion)
    cv2.setMouseCallback('Image', mouse)
    k=cv2.waitKey(1)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows()






            
