import cv2
import numpy

cap=cv2.VideoCapture(0)
#frame=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\orange.jpg")
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while True:
     
     ret,frame=cap.read()
     if ret==True:
      frame=cv2.resize(frame,(1280,720))
      h,w,c=frame.shape
      hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

      cw=int(w/2)
      ch=int(h/2)

      cv2.circle(frame,(cw,ch),5,(0,0,0),3)

      center_hsv_frame=hsv_frame[ch,cw]
      hue=center_hsv_frame[0]

      color='indifiend'
      if hue < 5:
         color= 'red'
      elif hue < 22:
         color= 'orange'
      elif hue < 33:
         color= 'yelow'
      elif hue < 78:
         color= 'green'
      elif hue < 131:
         color= 'blue'
      elif hue < 170:
         color= 'violet'
      else:
          color= "red"
      center_bgr_frame=frame[ch,cw]
      b=int(center_bgr_frame[0])
      g=int(center_bgr_frame[1])
      r=int(center_bgr_frame[2])    

      cv2.rectangle(frame,(cw-220,10),(cw+200,120),(255,255,255),-1)
      cv2.putText(frame,color,(cw-50,70),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(b,g,r),3)


     
      cv2.imshow('frame',frame)
      if cv2.waitKey(1)==ord('q'):
             break
     else:
         break
cap.release()
cv2.destroyAllWindows()