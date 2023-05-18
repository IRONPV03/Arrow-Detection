import cv2
import numpy as np

video=cv2.VideoCapture(0)

while True:
    ret,imgx=video.read()
    img=cv2.resize(imgx, (750,750))
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, bina= cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    a=(1,1,1)
    filt= np.array([a,a,a])
    s= bina.shape
    f= filt.shape
    bina= bina/255
    R= s[0] + f[0] -1
    C= s[1] + f[0] -1
    N= np.zeros((R,C))
    
    for i in range(s[0]):
        for j in range(s[1]):
            N[i+1, j+1]= bina[i,j]

    for i in range (s[0]):
        for j in range(s[1]):
            k=N[i:i+f[0],j:j+f[1]]
            result= (k==filt)
            final= np.all(result==True)
            if final:
                bina[i,j]=1
            else:
                bina[i,j]=0

    lower=np.array([0,50,50])
    upper=np.array([5,255,255])
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
                cv2.putText(img, 'Red arrow', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
                
            elif len(approx) == 8:
                cv2.putText(img, 'Octagon', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
            
            else:
                cv2.putText(img, 'Circle', (x+w+20, y+h+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1)
    cv2.imshow('Image', img)
    cv2.imshow('Mask', bina)
    k=cv2.waitKey(1000)
    if k==ord('d'):
        break
video.release()
cv2.destroyAllWindows()
