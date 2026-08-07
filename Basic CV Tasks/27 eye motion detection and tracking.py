import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    roi_bgr=frame[269:795,537:1416]
    r,c,_=roi_bgr.shape
    grey=cv2.cvtColor(roi_bgr,cv2.COLOR_BGR2GRAY)
    _,thres=cv2.threshold(grey,3,255,cv2.THRESH_BINARY_INV)
    contours,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contour:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(roi_bgr,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.line(roi_bgr,(0,y+int(h/2)),(c,y+int(h/2)),(0,255,0),3)
        cv2.line(roi_bgr,(x+int(w/2),0),(x+int(w/2),r),(0,255,0),3)

    if ret==True:
        cv2.imshow("frame",roi_bgr)
        if cv2.waitKey(20)==ord("q"):
            break
    else:
        break
cap.release
cv2.destroyAllWindows()