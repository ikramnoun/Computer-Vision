import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\sudoku.png",0)
#global thresholding
ret1,thres1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#otsu's thresholding
ret2,thres2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#blur
gussian=cv2.GaussianBlur(img,(5,5),0)
ret3,thres3=cv2.threshold(gussian,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles=["original","histogram","global threshold",
        "original","histogram","otsu's threshold",
        "gussian blur","histogram","otsu's threshold"]

images=[img,0,thres1,
        img,0,thres2,
        img,0,thres3]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],"gray")
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

''''
cv2.imshow("global thresholding",thres1)
cv2.imshow("otsu's thresholding",thres2)
cv2.imshow("otsu's+gussian",thres3)
cv2.waitKey(0)
'''