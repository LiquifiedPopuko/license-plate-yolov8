import easyocr
from thefuzz import process
from datetime import datetime
import requests
import re
import os
import csv

# be mindful of gpu
reader = easyocr.Reader(['th'], gpu=False)
url = 'todo.com'
license_data = csv.reader(open('./license/hi.csv'), delimiter=',')

# change file name and folder
def process_image(license_plate):
    predict_path = './runs/detect/predict/'
    current_date = datetime.now().strftime("%Y%m%dT%H%M%S")
    file_name = license_plate+'_'+current_date
    # rename file
    os.rename(predict_path+'image0.jpg', predict_path+file_name+'.jpg')
    # rename folder
    os.rename(predict_path, './runs/detect/'+file_name)
    return file_name

# check license plate data
def check_license(license_plate):
    for license in license_data:
        print("comparing: "+license[3]+' to '+license_plate)
        if license[3] == license_plate:
            return True
    return False


def get_license_id():
    license_id = 
    return license_id

# read license plate and return license plate results
def read_license_plate(license_plate):
   detections = reader.readtext(license_plate)
   results = [' ', None]

   print("Detections = "+ str(detections))

   # go through each license in case of multiple detections
   for detection in detections:
        print("Detection = "+str(detection))
        print("Score = "+str(detection[2]))
        # Must NOT have more than 15 characters
        if len(detection[1]) <= 15:
            if re.search("^\d?[ก-ฮ\d]{1,2}[\W-]\d{1,4}$", detection[1]) != None:
                results[0] = detection[1]
            elif re.search("^\d{1,4}$", detection[1]) != None:
                #insert last
                results[0] += detection[1]
            elif re.search("^\d?[ก-ฮ\d]{2}$",detection[1]) != None:
                #insert front
                results[0] = detection[1] + results[0]
            else:
                results[1] = match_province(detection[1])

   print("Detected:"+str(results))
   return results

# todo
def send_detection(license_number, province_id, access_type):
    obj = {
        'license_number': license_number,
        'province_id': province_id,
        'access_date': datetime.datetime.now(),
        'access_type': access_type
    }
    requests.post()

# match province
def match_province(province):
   provinces = ['กระบี่', 'กรุงเทพมหานคร', 'กาญจนบุรี', 'กาฬสินธุ์', 'กำแพงเพชร','ขอนแก่น','จันทบุรี','ฉะเชิงเทรา','ชลบุรี', 'ชัยนาท', 'ชัยภูมิ', 'ชุมพร', 'เชียงราย', 'เชียงใหม่','ตรัง', 'ตราด', 'ตาก','นครนายก', 'นครปฐม', 'นครพนม', 'นครราชสีมา', 'นครศรีธรรมราช', 'นครสวรรค์', 'นนทบุรี', 'นราธิวาส', 'น่าน','บึงกาฬ', 'บุรีรัมย์','ปทุมธานี', 'ประจวบคีรีขันธ์', 'ปราจีนบุรี', 'ปัตตานี','พระนครศรีอยุธยา', 'พะเยา', 'พังงา', 'พัทลุง', 'พิจิตร', 'พิษณุโลก', 'เพชรบุรี', 'เพชรบูรณ์', 'แพร่','ภูเก็ต','มหาสารคาม', 'มุกดาหาร', 'แม่ฮ่องสอน','ยโสธร', 'ยะลา','ร้อยเอ็ด', 'ระนอง', 'ระยอง', 'ราชบุรี','ลพบุรี', 'ลำปาง', 'ลำพูน', 'เลย','ศรีสะเกษ','สกลนคร', 'สงขลา', 'สตูล', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สระแก้ว', 'สระบุรี', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สุราษฎร์ธานี', 'สุรินทร์','หนองคาย', 'หนองบัวลำภู','อ่างทอง', 'อำนาจเจริญ', 'อุดรธานี', 'อุตรดิตถ์', 'อุทัยธานี', 'อุบลราชธานี']
   return process.extractOne(province, provinces)[0]
