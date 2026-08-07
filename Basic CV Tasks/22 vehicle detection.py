import cv2
import numpy as np

cap=cv2.VideoCapture(r"C:\computer vision\recurements\video (2).mp4",0)
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()
detect=[]
count=0
while True:
    ret,frame=cap.read()
    if ret ==True:
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(grey,(5,5),5)
        bgs=subtracao.apply(blur)
        dilation=cv2.dilate(bgs,np.ones((5,5)))
        contours,_=cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame,(25,550),(1200,550),(255,0,0),2)
        for (i,c) in enumerate(contours):
            x,y,w,h=cv2.boundingRect(c)
            cx=x+int(w/2)
            cy=y+int(h/2)
            if w>=80 and h>=80:
                cv2.rectangle(frame,(x,y),(x+w,h+y),(0,255,0),2)
                cv2.circle(frame,(cx,cy),4,(0,0,255),-1)
                detect.append([cx,cy])
        for x,y in detect:
            if y<=556 and y>=544:
                count+=1
                cv2.line(frame,(25,550),(1200,550),(0,255,255),2)
                detect.remove([x,y])
        cv2.putText(frame,"nbr of vehicles:"+str(count),(600,60),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),2)


          
      


        cv2.imshow("video",frame)
        cv2.imshow("subtractore",bgs)
        cv2.imshow("dilation",dilation)
        
        if cv2.waitKey(20)==ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows