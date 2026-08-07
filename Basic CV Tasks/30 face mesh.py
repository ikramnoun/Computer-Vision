import cv2
import numpy as np
import mediapipe as mp


mp_face_mesh=mp.solutions.face_mesh.FaceMesh()
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    if ret==True:

        rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        res=mp_face_mesh.process(rgb_img)
        h,w,_=img.shape
        
        for facial_landmarks in res.multi_face_landmarks:
            for i in range(0,468):
                pt=facial_landmarks.landmark[i]
                x=int(pt.x*w)
                y=int(pt.y*h)
                cv2.circle(img,(x,y),2,(100,100,0),-1)
        
        cv2.imshow("face_mesh",img)
        if cv2.waitKey(1)==ord("q"):
            break
    else:
        break
cap.release
cv2.destroyAllWindows()