import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\lena.jpg")
#b,g,r=cv2.split(img)

#img=np.zeros((500,500),np.uint8)
#cv2.rectangle(img,(0,250),(500,500),(255),-1)
#cv2.rectangle(img,(0,127),(250,250),(127),-1)
'''
plt.hist(img.ravel(),255,[0,255])
plt.hist(b.ravel(),255,[0,255])
plt.hist(g.ravel(),255,[0,255])
plt.hist(r.ravel(),255,[0,255])
'''
hist=cv2.calcHist(img,[2],None,[255],[0,255])
plt.plot(hist)
plt.show()

cv2.imshow("img",img)
#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)
cv2.waitKey(0)