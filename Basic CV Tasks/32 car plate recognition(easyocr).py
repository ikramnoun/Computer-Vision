import cv2
import numpy as np
import imutils
import easyocr

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\32544764_7.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bilateralfilter=cv2.bilateralFilter(gray,11,17,17)
canny=cv2.Canny(bilateralfilter,30,100)

keypoints=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(keypoints)
contour=sorted(contours,key=cv2.contourArea,reverse=True)[:10]

loc=None
for cnt in contour:

    approx=cv2.approxPolyDP(cnt,10,True)

    if len(approx)==4:
        loc=approx
        #cv2.drawContours(img,[loc],-1,(255),3)
        break

mask=np.zeros(gray.shape,np.uint8)
new_img=cv2.drawContours(mask,[loc],-1,(255),-1)
new_img=cv2.bitwise_and(img,img,mask=mask)

(x,y)=np.where(mask==255)
(x1,y1)=(np.min(x),np.min(y))
(x2,y2)=(np.max(x),np.max(y))
cropped=gray[x1:x2,y1:y2]

reader=easyocr.Reader(["en"])
res=reader.readtext(cropped)
print(res)

text=res[0][-2]
cv2.putText(img,text,(x1,y1-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
cv2.rectangle(img,tuple(approx[0][0]),tuple(approx[2][0]),(0,255,0),2)



cv2.imshow("img",img)
#cv2.imshow("biltrafilter",bilateralfilter)
cv2.imshow("edges",canny)
#cv2.imshow("mask",mask)
cv2.imshow("bitwise",new_img)
cv2.imshow("cropped",cropped)

cv2.waitKey(0)