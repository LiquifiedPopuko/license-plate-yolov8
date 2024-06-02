from firebase_admin import credentials, initialize_app, storage
# Init firebase with your credentials
cred = credentials.Certificate("./module/smart-parking-21e9b-firebase-adminsdk-cmymm-d701fc4c06.json")
app = initialize_app(cred, {'storageBucket': 'smart-parking-21e9b.appspot.com'})

destination_path = './license/hi.csv'
storage_path = 'license/hi.csv'

bucket = storage.bucket()
blob = bucket.blob(storage_path)
blob.download_to_filename(destination_path)