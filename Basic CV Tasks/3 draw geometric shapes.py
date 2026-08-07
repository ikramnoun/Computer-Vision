import cv2
import numpy as np

mask=np.zeros([480,640,3],np.int8)

sky=cv2.rectangle(mask,(0,0),(640,200),(255,0,0),-1)
ground=cv2.rectangle(mask,(0,200),(640,480),(0,255,0),-1)
sun=cv2.circle(mask,(100,100),50,(0,255,255),-1)
sunlight=cv2.circle(mask,(100,100),65,(255,244,255),10)
#tree1
pts=np.array([[540,420],[600,420],[570,200]],np.int32)
tree=cv2.fillPoly(mask,[pts],(75,180,70))
line=cv2.line(mask,(570,420),(570,480),(30,65,155),15)
#tree2
pts=np.array([[440,420],[550,420],[495,100]],np.int32)
tree=cv2.fillPoly(mask,[pts],(75,255,70))
line=cv2.line(mask,(495,420),(495,480),(30,65,155),15)

text=cv2.putText(mask,'i love python',(50,200),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(200,180,0),2)

cv2.imwrite('tree.png',mask)
cv2.imshow('mask',mask)
cv2.waitKey(0)