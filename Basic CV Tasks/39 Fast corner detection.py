import cv2
import numpy as np

img= cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\OIP-C.webp")

fast= cv2.FastFeatureDetector_create()

kp= fast.detect(img)
img2= cv2.drawKeypoints(img,kp,None,color=(0,0,255))

print("threshold:{}" .format(fast.getThreshold()))
print("nonmaxsuppression: {}" .format(fast.getNonmaxSuppression()))
print("neighborhood: {}" .format(fast.getType()))
print("total keypoints with nms: {}" .format(len(kp)))

fast.setNonmaxSuppression(0)
kp1= fast.detect(img, None)
img3= cv2.drawKeypoints(img,kp1,None, color=(0,0,255))

print("total keypoints without nms: {}" .format(len(kp1)))

cv2.imshow("edges with nms", img2)
cv2.imshow("edges without nms", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()