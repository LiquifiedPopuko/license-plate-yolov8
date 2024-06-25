import numpy as np
import cv2
import util
import upload
import cleanup
import display
from datetime import datetime
from ultralytics import YOLO
import queue_service

cleanup.cleanup()

cap = cv2.VideoCapture(11)

# load models
print("Loading Model...")
model_path = './model/license_detector.pt'
model = YOLO(model_path)  # pretrained YOLOv8n model
print("Loading Model - Done")
print("Start recording")

results_path = './output/'

while (True):
    # Capture frame-by-frame
    ret1, frame = cap.read()
    image = display.get_state_image()

    # resize image
    img_height = 240
    img_width = 240
    image = cv2.resize(image, (img_width,img_height))

    # Display the resulting frame
    white_color = [255,255,255]
    left = int(frame.shape[1]) # shape[1]
    dst = cv2.copyMakeBorder(frame, 0, 0, left, 0, cv2.BORDER_CONSTANT, None, white_color)
    dst[120:img_width+120, 240:img_height+240] = image
    cv2.imshow('Main', dst)

    # Press Q to detect license plate
    if cv2.waitKey(1) & 0xFF == ord('q'):
        start_time = datetime.now() 
        print("Capturing")
        i = 0
        detections = model.predict(frame, save=True, show_boxes=True)
        for detection in detections[0].boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection

            access_history = {
                "license_id": None, 
                "access_date": None, 
                "access_type": None, 
                "image_source": None
            }
            
            access_history["access_type"] = 2
            access_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            access_history["access_date"] = access_date

            # crop license plate
            img_path = results_path + str(i) + '.jpg'
            i += 1
            license_plate = frame[int(y1):int(y2), int(x1):int(x2), :]

            # process license plate
            license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)

            result = util.read_license_plate(license_plate)

            # temp
            license_scan = util.check_license(result[0])
            print(license_scan[0])
            print("setting image stage")
            display.set_access_image_state(license_scan[0])
            access_history["license_id"] = license_scan[1]
            
            # rename file & folder to proper format
            file_name = util.process_image(result[0], access_date)

            # upload file to firebase storage
            access_history["image_source"] = upload.upload_image(file_name)
            print(upload.upload_image(file_name))

            queue_service.add_queue(access_history)
            
            # save crop
            cv2.imwrite(img_path, license_plate)

        end_time = datetime.now()
        time_difference = (end_time - start_time).total_seconds() * 10**3
        print("Execution time of capture is: ", time_difference, "ms") 
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
