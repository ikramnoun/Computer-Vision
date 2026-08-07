import cv2 
import numpy as np

cap=cv2.VideoCapture(0)
face_detection=cv2.CascadeClassifier(r"C:\computer vision\recurements\haarcascade_frontalface_default.xml")
eye_detection=cv2.CascadeClassifier(r"C:\computer vision\recurements\haarcascade_eye.xml")
while True:
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_detection.detectMultiScale(gray,1.1,4)
        
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"face",(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            
            eye=eye_detection.detectMultiScale(gray,2.3,4)
            for (ex,ey,ew,eh) in eye:
              cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
              cv2.putText(frame,"eye",(ex,ey-3),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

        cv2.imshow("frame",frame)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break
cap.release
cv2.destroyAllWindows()
    