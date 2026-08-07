import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\shappes.jpg")
#blur=cv2.GaussianBlur(img,(5,5),0)
#cv2.imshow('blur',blur)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
ret,thres=cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thres",thres)
contours,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)
for i in range(len(contours)):
    hull=cv2.convexHull(contours[i])
    cv2.drawContours(img,[hull],-1,(255,0,0),3)
cv2.imshow("convexhull",img)
cv2.waitKey(0)
