import easyocr
from thefuzz import process
import datetime
import requests
import re

# be mindful of gpu
reader = easyocr.Reader(['th'], gpu=False)
url = 'todo.com'

# todo
def check_database():
   return

# read license plate and return license plate results
def read_license_plate(license_plate):
   detections = reader.readtext(license_plate)
   results = []

   print("Detections = "+ str(detections))

   # go through each license in case of multiple detections
   for detection in detections:

      print("Detection = "+str(detection))
      print("Score = "+str(detection[2]))
      # confidence threshold, skip when less than 70%
      if 0.7 > float(detection[2]):
         print("Skip")
         continue

      # detection[1] is the text result of the detection i.e, "กรุงเทพมหานคร"
      # verify if license plate is in correct format to avoid mistaking other inputs
      # if is_license_data(detection[1]):
      #    results.append(detection[1])

      results.append(detection[1])

   print("Detected:"+str(results))

   return results

# check if the string is a license plate
def is_license_data(license):
    return re.search("\d?[ก-ฮ\d]{1,2}[\s-]\d{1,4}", license)

# check if the string is province
def is_province(province):
    return re.search("[ก-ํ]+", province)

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

    provinces = ['กระบี่', 'กรุงเทพมหานคร', 'กาญจนบุรี', 'กาฬสินธุ์', 'กำแพงเพชร',
                 'ขอนแก่น',
                 'จันทบุรี',
                 'ฉะเชิงเทรา',
                 'ชลบุรี', 'ชัยนาท', 'ชัยภูมิ', 'ชุมพร', 'เชียงราย', 'เชียงใหม่',
                 'ตรัง', 'ตราด', 'ตาก',
                 'นครนายก', 'นครปฐม', 'นครพนม', 'นครราชสีมา', 'นครศรีธรรมราช', 'นครสวรรค์', 'นนทบุรี', 'นราธิวาส', 'น่าน',
                 'บึงกาฬ', 'บุรีรัมย์',
                 'ปทุมธานี', 'ประจวบคีรีขันธ์', 'ปราจีนบุรี', 'ปัตตานี',
                 'พระนครศรีอยุธยา', 'พะเยา', 'พังงา', 'พัทลุง', 'พิจิตร', 'พิษณุโลก', 'เพชรบุรี', 'เพชรบูรณ์', 'แพร่',
                 'ภูเก็ต',
                 'มหาสารคาม', 'มุกดาหาร', 'แม่ฮ่องสอน',
                 'ยโสธร', 'ยะลา',
                 'ร้อยเอ็ด', 'ระนอง', 'ระยอง', 'ราชบุรี',
                 'ลพบุรี', 'ลำปาง', 'ลำพูน', 'เลย',
                 'ศรีสะเกษ',
                 'สกลนคร', 'สงขลา', 'สตูล', 'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สระแก้ว', 'สระบุรี', 'สิงห์บุรี', 'สุโขทัย', 'สุพรรณบุรี', 'สุราษฎร์ธานี', 'สุรินทร์',
                 'หนองคาย', 'หนองบัวลำภู',
                 'อ่างทอง', 'อำนาจเจริญ', 'อุดรธานี', 'อุตรดิตถ์', 'อุทัยธานี', 'อุบลราชธานี']

    # choose most likely province
    return process.extractOne(province, provinces, score_cutoff=0.7)
