import cv2
import numpy  as np
import keras_ocr
from matplotlib import pyplot as plt

pipeline=keras_ocr.pipeline.Pipeline()

img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\Good-Advice-Quotes-1024x576 (2).jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
predection=pipeline.recognize(gray)

fig,axs=plt.subplot(nrows=len(img),figsize=(20,20))
for ax,image,pre in zip(axs,gray,predection):
    keras_ocr.tools.drawAnnotations(image=image,predections=pre,ax=ax)

#cv2.imshow("img",img)
#cv2.waitKey(0)