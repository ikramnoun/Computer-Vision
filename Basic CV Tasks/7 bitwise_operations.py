import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=np.full((250,500,3),255,np.uint8)
cv2.rectangle(img2,(0,0),(250,250),(0,0,0),-1)

andOp=cv2.bitwise_and(img1,img2)
orOp=cv2.bitwise_or(img1,img2)
xorOp=cv2.bitwise_xor(img1,img2)
notOp=cv2.bitwise_not(img1)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('and',andOp)
cv2.imshow('or',orOp)
cv2.imshow('xor',xorOp)
cv2.imshow('not',notOp)
cv2.waitKey(0)