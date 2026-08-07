import cv2
import matplotlib.pyplot as plt
import numpy as np

img1= cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\Screenshot-2024-05-29-094049-(1).png")
img2= cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\Screenshot-2024-05-29-094024-(1).png")

orb= cv2.ORB_create()

kp1, des1= orb.detectAndCompute(img1,None)
kp2, des2= orb.detectAndCompute(img2, None)
#img= cv2.drawKeypoints(img2, kp2, None, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

bf= cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

matches= bf.match(des1, des2)
matches= sorted(matches, key= lambda x: x.distance)

img3= cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)
img3= cv2.resize(img3,(640,480))

cv2.imshow("matches",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()