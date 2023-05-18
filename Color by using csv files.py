#This program used to take csv file of color from the user and print the
#color to the user with the shape.

import cv2
import numpy as np
import pandas as pd

r = g = b = xpos = ypos = 0
clicked = False
def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDCLICK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)



img = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\Society Project\Shapes 12.png")
csv_path = r'C:\Users\DELL\OneDrive\Desktop\Society Project\colors.csv'
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thrash = cv2.threshold(img_grey,240,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thrash ,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
l = []

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)
cv2.namedWindow('Shapes')
cv2.setMouseCallback("Shapes", draw_function)

for contour in contours:
    '''
    For shape detection
    '''
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,255,0) ,2)
    x,y = approx.ravel()[0],approx.ravel()[1]
    aplen = len(approx)
    l.append(aplen)
    

    if (aplen == 3):
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    elif (aplen == 4):
        cv2.putText(img, "Quadilateral", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    elif (aplen == 5):
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    elif (aplen == 6):
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    elif (aplen == 8):
        cv2.putText(img, "Octagon", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    elif (aplen == 10):
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0))

while True:
    cv2.imshow("Shapes",img)
    
    if clicked:
        cv2.rectangle(img, (20,20), (300,60), (b,g,r), -1)
        text =' (' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        cv2.putText(img,text,(50,50), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,255,0))
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
    
print(*l)

cv2.waitKey(0)
cv2.destroyAllWindows()
