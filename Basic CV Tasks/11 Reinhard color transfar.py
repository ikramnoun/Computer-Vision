import numpy as np
import cv2
import os
os.chdir(r"C:\computer vision\recurements\rein hard clolr transfar")

input_dir = "input images"
#input_dir = "pathology_input/"
input_image_list = os.listdir(input_dir)

output_dir = "C:\computer vision\recurements\rein hard clolr transfar\output images"


def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2)) 
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

template_img = cv2.imread(r"templet images\428690.jpg",1)
template_img=cv2.resize(template_img,(640,480))
cv2.imshow('templet image',template_img)
template_img = cv2.cvtColor(template_img,cv2.COLOR_BGR2LAB)
template_mean, template_std = get_mean_and_std(template_img)

for img in (input_image_list):
    print(img)
    input_img = cv2.imread(r"input images\pngtree-beautiful-train-tracks-that-lead-into-deep-green-forest-image_2530076.png",1)
    #input_img = cv2.imread(input_dir+img)
    input_img=cv2.resize(input_img,(640,480))
    cv2.imshow('target image',input_img)
    input_img = cv2.cvtColor(input_img,cv2.COLOR_BGR2LAB)
    
    
    img_mean, img_std = get_mean_and_std(input_img)
    
    
    height, width, channel = input_img.shape
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,channel):
            	x = input_img[i,j,k]
                # print("x",x)
            	x = ((x-img_mean[k])*(template_std[k]/img_std[k]))+template_mean[k]
            	x = round(x)
            	# boundary check
            	x = 0 if x<0 else x
            	x = 255 if x>255 else x
            	input_img[i,j,k] = x
            
    input_img= cv2.cvtColor(input_img,cv2.COLOR_LAB2BGR)
    cv2.imshow("output",input_img)
    cv2.imwrite(output_dir+"modified_"+img, input_img)
    cv2.waitKey(0)