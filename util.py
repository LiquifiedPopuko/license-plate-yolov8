import easyocr

#be mindful of gpu
reader = easyocr.Reader(['th'], gpu=False)

def read_license_plate(license_plate):
   detections = reader.readtext(license_plate)
   results = []
   for detection in detections:
      results.append(detection[1])
   return results

# match province
def match_province():
   return