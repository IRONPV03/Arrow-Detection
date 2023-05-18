#This was used to display the shape of predefined image

import cv2 as cv
import numpy as np
  
img= cv.imread(r'C:\Users\DELL\OneDrive\Desktop\Society Project\Shapes 12.png')
imgx= cv.resize(img, (750,750)) 
gray = cv.cvtColor(imgx, cv.COLOR_BGR2GRAY)
  
_,threshold = cv.threshold(gray, 245, 255, cv.THRESH_BINARY)
  
contours,_= cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
  
i = 0
for contour in contours:
    if i == 0:
        i = 1
        continue  
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
      
    cv.drawContours(imgx, [approx], 0, (0, 0, 255), 1)

    M = cv.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
    
  
    if len(approx) == 3:
        cv.putText(imgx, 'Triangle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
  
    elif len(approx) == 4:
        a,b,w,h= cv.boundingRect(approx)
        ar=w/h
        if ar==1:
            cv.putText(imgx, 'Square', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
        else:
            cv.putText(imgx, 'Rectangle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
                      
    elif len(approx) == 5:
        cv.putText(imgx, 'Pentagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
                      
    elif len(approx) == 6:
        cv.putText(imgx, 'Hexagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
                      
    elif len(approx) == 7:
        cv.putText(imgx, 'Heptagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
        
    elif len(approx) == 8:
        cv.putText(imgx, 'Octagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
        
    else :
        cv.putText(imgx, 'Circle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)

cv.imshow('Shapes', imgx)
cv.waitKey(0)

