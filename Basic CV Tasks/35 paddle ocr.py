import cv2
import numpy as np
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image,ImageDraw,ImageFont

ocr = PaddleOCR(use_angle_cls=True, lang='en')

img_path=r"C:\Users\Dell Latitude E5470\Pictures\Good-Advice-Quotes-1024x576 (2).jpg"
img=cv2.imread(img_path,-1)

res=ocr.ocr(img_path,cls=True)
#for line in res:
    #print(line)

image = Image.open(img_path).convert('RGB')

boxes = [line[0] for line in res]
txts = [line[1][0] for line in res]
scores = [line[1][1] for line in res]
font = ImageFont.load_default()
im_show = draw_ocr(image, boxes, txts, scores,font_path='/usr/share/fonts/truetype/humor-sans/Humor-Sans.ttf' )
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
