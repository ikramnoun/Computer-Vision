import cv2
import numpy as np
import time

cap = cv2.VideoCapture("video (1).mp4",0)
#cap = cv2.VideoCapture(0)
#cap=cv2.VideoCapture("http://10.63.42.74:8080/video")
net = cv2.dnn.readNetFromONNX("C:\yolov5\yolov5n.onnx")
file = open("C:\yolov5\coco.txt","r")
classes = file.read().split('\n')
#print(classes)
time_start=time.time()
frame_id=0
font=cv2.FONT_HERSHEY_COMPLEX

while True:
    img = cap.read()[1]
    frame_id+=1
    if frame_id%3!=0:
        continue
    if img is None:
        break
    img = cv2.resize(img, (640,480))
    blob = cv2.dnn.blobFromImage(img,scalefactor= 1/255,size=(640,640),mean=[0,0,0],swapRB= True, crop= False)
    net.setInput(blob)
    detections = net.forward()[0]
  

    # cx,cy , w,h, confidence, 80 class_scores
    # class_ids, confidences, boxes

    classes_ids = []
    confidences = []
    boxes = []
    rows = detections.shape[0]

    img_width, img_height = img.shape[1], img.shape[0]
    x_scale = img_width/640
    y_scale = img_height/640

    for i in range(rows):
        row = detections[i]
        confidence = row[4]
        if confidence > 0.5:
            classes_score = row[5:]
            ind = np.argmax(classes_score)
            if classes_score[ind] > 0.5:
                classes_ids.append(ind)
                confidences.append(confidence)
                cx, cy, w, h = row[:4]
                x1 = int((cx- w/2)*x_scale)
                y1 = int((cy-h/2)*y_scale)
                width = int(w * x_scale)
                height = int(h * y_scale)
                box = np.array([x1,y1,width,height])
                boxes.append(box)

    indices = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.5)
    
    for i in indices:
        x1,y1,w,h = boxes[i]
        label = classes[classes_ids[i]]
        conf = confidences[i]
        text = label + "{:.2f}".format(conf)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(255,0,0),2)
        cv2.putText(img, text, (x1,y1-2),font, 0.7,(255,0,255),2)
    elp_time=time.time()-time_start
    fps=frame_id/elp_time
    cv2.putText(img,"fps="+str(fps),(20,30),1,font,(0,255,0),2)

    cv2.imshow("VIDEO",img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break