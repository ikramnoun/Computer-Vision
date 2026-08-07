import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\shappes.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thres=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contoures,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contoures:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    cv2.drawContours(img,[cnt],0,(255,0,0),3)
    if len(approx)==3:
        cv2.putText(img,"traingle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
    elif len(approx)==10:
        cv2.putText(img,"star",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
    elif len(approx)==5:
        cv2.putText(img,"pentagone",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
    elif len(approx)==4:
        x1,y1,w,h=cv2.boundingRect(cnt)
        ratio=float(w/h)
        if ratio>=0.95 and ratio<=1.05:
            cv2.putText(img,"square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
        else:
            cv2.putText(img,"rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),3)
cv2.imshow("shapes",img)
cv2.waitKey(0)