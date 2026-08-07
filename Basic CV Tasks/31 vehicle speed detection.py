import cv2
import numpy as np
import time

cap=cv2.VideoCapture(r"C:\Users\Dell Latitude E5470\Downloads\video3.mp4",0)
cascade=cv2.CascadeClassifier(r"C:\computer vision\recurements\haarcascade_cars.xml")
start_time=time.time()



def speed_cal(time):
    try:
       speed=(9.144/1000)/(time/3600)
       return speed
    except ZeroDivisionError:
        print("can't detect speed")
i=1
while True:
    ret,frame=cap.read()
    if ret==True:

        #frame=cv2.resize(frame,(512,512))
        blur=cv2.blur(frame,(15,15))
        gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
        cars=cascade.detectMultiScale(gray,1.1,5)
        
        cv2.line(frame,(70,90),(230,90),(255,0,0),3)
        cv2.line(frame,(15,125),(225,125),(255,0,0),3)
        
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.circle(frame,(int((w+x+x)/2),int((y+y+h)/2)),3,(0,255,0),-1)        
    
            while int((y+y+h)/2)==int(90):
               cv2.line(frame,(70,90),(230,90),(0,255,0),3)
               start_time==time.time()
               break
            
            #while int((y+y+h)/2)>=int(90):
            if int((y+y+h)/2)>=int(125) and int((y+y+h)/2)<=int(135):
                cv2.line(frame,(15,125),(225,125),(0,255,0),3)
                speed=speed_cal(time.time()-start_time)
                cv2.putText(frame,"speed"+str(speed)+"km/h",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
                print("speed:",speed)
                #i=i+1
                #break


        cv2.imshow("frame",frame)
        if cv2.waitKey(40)==ord("q"):
            break
    else:
        break
cap.release
cv2.destroyAllWindows()
