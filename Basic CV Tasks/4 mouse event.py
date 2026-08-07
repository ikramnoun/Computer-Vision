import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in  i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        cv2.circle(img,(x,y),13,(255,0,0),-1)
        pts.append((x,y))
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        if len(pts)>=2:
            
            cv2.line(img,pts[-1],pts[-2],(0,255,255),3)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        color = np.zeros((512, 512, 3), np.uint8)
        color[:]=[blue,green,red]
    
        cv2.imshow('image', img)
        cv2.imshow('color',color)
        
img=cv2.imread(r"apple.jpg",1)
pts= []

#frameCounter = 0
#cap = cv2.VideoCapture(r"C:\Users\Dell Latitude E5470\Downloads\vid1.mp4",0)
#while True:
 #   frameCounter +=1
  #  if cap.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
   #  cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    # frameCounter=0
    #ret,img=cap.read()
    #img=cv2.resize(img,(640,480))
    #if ret==True:
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
        
#        if cv2.waitKey(1)==ord("q"):
 #        break
  #  else:
   #     break

cv2.waitKey(0)
#cv2.destroyAllWindows()