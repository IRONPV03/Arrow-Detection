#This function was made to judge the angle using onlick function

import cv2
import math
import numpy as np

points=[]
angd=0
video=cv2.VideoCapture(0)
while True:
    ret,imgx=video.read()
    img=cv2.resize(imgx, (1000,750))
    cv2.line(img, (500,0), (500,750),(0,255,0), 1)
    cv2.line(img, (0,375), (1000,375),(0,255,0), 1)

    points=[(500,375), (750,375)]
    def mouse(e, x, y, d, f):
        if e==cv2.EVENT_LBUTTONDOWN:
            points.append([x,y])
            cv2.imshow('Image',img)
            degrees=angle()
            print(degrees)
    cv2.putText(img, str(angd), (10,700), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,255), 1)
    def angle():
        global angd
        a=points[0]
        b=points[1]
        c=points[2]
        m1= (a[1]-b[1])/(a[0]-b[0])
        m2= (a[1]-c[1])/(c[0]-a[0])
        angr= math.atan((m2-m1)/1+m1*m2)
        angd=round(math.degrees(angr))
        if c[0]==500 and c[1]<375:
            angd=0
        elif c[0]>500 and c[1]<375:
            angd=90-angd
        elif c[0]>500 and c[1]==375:
            angd=90
        elif c[0]>500 and c[1]>375:
            angd=90+abs(angd)
        elif c[0]>500 and c[1]>375:
            angd=180
        elif c[0]<500 and c[1]>375:
            angd=270-angd
        elif c[0]<500 and c[1]==375:
            angd=270
        else:
            angd=270+abs(angd)
        return angd
    k=cv2.waitKey(1)
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mouse)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows()


