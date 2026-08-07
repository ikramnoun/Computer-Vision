import cv2
import numpy
from matplotlib import pyplot as plt

img= cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\lena.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

blur=cv2.blur(img,(5,5))   #mean for pixles
g_blur=cv2.GaussianBlur(img,(5,5),0)   #for noise images
medain_blur=cv2.medianBlur(img,5)   #for salt images
bilateralFilter=cv2.bilateralFilter(img,9,75,75)
convoltion=cv2.filter2D(img,-1,(5,5))

titles=["original",'blur',"gusian_blur",'medain_blur',"bilateralFilter","2D_convolution"]
images=[img,blur,g_blur,medain_blur,bilateralFilter,convoltion]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()