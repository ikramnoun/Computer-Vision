import cv2
import numpy as np

img= cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\00pedxing01-superJumbo.jpg")
img= cv2.resize(img, (640,480))

hog= cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(bounding_boxes, weights)= hog.detectMultiScale(img, winStride=(4,4), padding= (8,8), scale= 1.05)

for (x,y,w,h) in bounding_boxes:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),4)


cv2.imshow("hog", img)
cv2.waitKey(0)
cv2.destroyAllwindow()