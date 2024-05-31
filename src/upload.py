from firebase_admin import credentials, initialize_app, storage
# Init firebase with your credentials
cred = credentials.Certificate("./module/smart-parking-21e9b-firebase-adminsdk-cmymm-d701fc4c06.json")
app = initialize_app(cred, {'storageBucket': 'smart-parking-21e9b.appspot.com'})
file_path = "./runs/detect/"

# Put your local file path 
def upload_image(file):
   bucket = storage.bucket()
   blob = bucket.blob("images/"+file)
   blob.upload_from_filename(file_path+file)
   # Opt : if you want to make public access from the URL
   blob.make_public()
   return blob.public_url