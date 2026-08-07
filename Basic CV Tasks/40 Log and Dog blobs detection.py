import cv2
import numpy as np

img= cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\R.jpg")

params= cv2.SimpleBlobDetector_Params()

params.minThreshold= 0
params.maxThreshold= 255

params.filterByArea = True
params.minArea= 50
params.maxArea= 10000

params.filterByColor = False
params.blobColor = 0

params.filterByCircularity = True
params.minCircularity = 0.5
params.maxCircularity = 1

params.filterByConvexity = True
params.minConvexity = 0.1

detector= cv2.SimpleBlobDetector_create(params)

keypoints= detector.detect(img)

img_with_blobs= cv2.drawKeypoints(img, keypoints, None, (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print("number of blobs:", len(keypoints))

cv2.imshow("keypoints", img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()