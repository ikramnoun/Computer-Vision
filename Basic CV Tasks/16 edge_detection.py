import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\messi5.jpg",0)

laplacian=cv2.Laplacian(img,cv2.CV_64F,3)
laplacian=np.uint8(np.absolute(laplacian))

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1)
sobel_x=np.uint8(np.absolute(sobel_x))
sobel_y=np.uint8(np.absolute(sobel_y))
combined_edge=cv2.bitwise_or(sobel_x,sobel_y)

canny=cv2.Canny(img,100,200)

titles=["Original Image","Laplacian Edge Detection","X Sobel-Edge","Y Sobel-Edge","combinedSobel","canny_edge"]
images=[img,laplacian,sobel_x,sobel_y,combined_edge,canny]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()