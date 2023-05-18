#This was the first thing I learnt while learning opencv

import cv2 as cv

#for image reading
img = cv.imread(r'C:\Users\DELL\OneDrive\Desktop\Society Project\Blue circle.png')
cv.imshow('Circle', img)
cv.waitKey(0)

#for resizing the video
def rescaleFrame(frame, scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions= (width,height)

    return cv.resize(frame, dimensions)

#for resizing image
img_resized=rescaleFrame(img)
cv.imshow('Image resized', img_resized)

#for video reading
cap= cv.VideoCapture(r'C:\Users\DELL\OneDrive\Desktop\Society Project\Farewell 1.mp4')
while True:
    isTrue, frame = cap.read()
    frame_resized=rescaleFrame(frame, scale=0.75)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()

