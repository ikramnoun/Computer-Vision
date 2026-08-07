import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\R (2).jpg")  #eng
#img=cv2.imread(r"C:\Users\Dell Latitude E5470\Pictures\OIP (3).jpg")  #chi_sim
img=cv2.imread(r"C:\Users\Dell Latitude E5470\Downloads\Arabic_OCR.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
config="--psm 3"
text=pytesseract.image_to_string(img,lang="ara",config=config)
print(text)
cv2.imshow("gray",gray)
cv2.waitKey(0)