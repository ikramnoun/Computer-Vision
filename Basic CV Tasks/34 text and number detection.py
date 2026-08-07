import cv2
import numpy as np
import pytesseract

#img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\R (2).jpg")
img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\41a93763336ffbe49ccd1e4b8209464c.png")
r,c,_=img.shape
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

'''
boxes=pytesseract.image_to_boxes(gray)
#print(boxes)
for b in boxes.splitlines():
 #   print(b)
    b=b.split(" ")
    #print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,r-y),(w,r-h),(0,255,0),2)
    cv2.putText(img,b[0],(x,r-y+10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
'''

'''
words=pytesseract.image_to_data(gray)
#print(boxes)
for x,b in enumerate(words.splitlines()):
 if x!=0:
    b=b.split()
    #print(b)
    x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
    if len(b)==12:
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
     cv2.putText(img,b[11],(x,y+10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
'''

'''
config=r"--oem 3 --psm 6 outputbase digits"
boxes=pytesseract.image_to_data(gray,lang="eng",config=config)
#print(boxes)
for x,b in enumerate(boxes.splitlines()):
 #   print(b)
 if x!=0:
    b=b.split()
    #print(b)
    x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
    if len(b)==12:
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
     cv2.putText(img,b[11],(x,y+10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
'''

config=r"--oem 3 --psm 6 outputbase digits"
boxes=pytesseract.image_to_boxes(gray,lang="eng",config=config)
#print(boxes)
for b in boxes.splitlines():
 #   print(b)
    b=b.split(" ")
    #print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,r-y),(w,r-h),(0,255,0),2)
    cv2.putText(img,b[0],(x,r-y+10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow("img",img)
cv2.waitKey(0)