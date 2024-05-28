from firebase_admin import credentials, initialize_app, storage
# Init firebase with your credentials
cred = credentials.Certificate(".module/smart-parking-21e9b-firebase-adminsdk-cmymm-d701fc4c06.json")
initialize_app(cred, {'storageBucket': 'smart-parking-21e9b.appspot.com'})

# Put your local file path 
def upload_image(file):
   bucket = storage.bucket()
   blob = bucket.blob(file)
   blob.upload_from_filename(file)
   # Opt : if you want to make public access from the URL
   blob.make_public()
   return blob.public_url

