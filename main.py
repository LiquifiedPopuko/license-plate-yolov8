from ultralytics import YOLO
import cv2
import util
import numpy as np

#load models
model_path = './model_testing/license_detector.pt'
model = YOLO(model_path)  # pretrained YOLOv8n model

#load video (img for now)
#read frames
#detect license plates
img = cv2.imread('./model_testing/IMG_test2.jpg')
#img = './model_testing/IMG_test.jpg'
detections = model(img)

results_path = './results/'
i = 0

#detections[0] is TEMPorary
#license plate detection and crop
for detection in detections[0].boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = detection

    #crop license plate
    img_path = results_path + str(i) + '.jpg'
    i+=1
    license_plate = img[int(y1):int(y2), int(x1):int(x2), :]

    #process license plate
    license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
    
    result = util.read_license_plate(license_plate)
    print(str(result))
    #save crop
    cv2.imwrite(img_path, license_plate)

#write results