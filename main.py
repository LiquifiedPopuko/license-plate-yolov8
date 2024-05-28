import numpy as np
import cv2
import util
import os
from datetime import datetime
from ultralytics import YOLO

cap = cv2.VideoCapture(0)

# load models
print("Loading Model...")
model_path = './model_testing/license_detector.pt'
model = YOLO(model_path)  # pretrained YOLOv8n model
print("Loading Model - Done")
print("Start recording")

predict_path = './runs/detect/predict/'
results_path = './results/'

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)

    # Press Q to detect license plate
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Capturing")
        i = 0
        detections = model.predict(frame, save=True, show_boxes=True)
        for detection in detections[0].boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection

            # crop license plate
            img_path = results_path + str(i) + '.jpg'
            i += 1
            license_plate = frame[int(y1):int(y2), int(x1):int(x2), :]

            # process license plate
            license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)

            result = util.read_license_plate(license_plate)
            print(str(result))
            os.rename(predict_path+'image0.jpg', predict_path+str(result[0])+datetime.now().strftime("_%Y%m%dT%H%M%S")+'.jpg')
            # save crop
            cv2.imwrite(img_path, license_plate)
        print("License capture - Done")

    # Press R to quit
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print("break")
        break

print("Closing")
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print("Closing Done")
