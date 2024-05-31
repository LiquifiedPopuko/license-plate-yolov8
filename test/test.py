import unittest
from src.upload import upload_image

class Test1(unittest.TestCase):

   def test_upload_image(self):
      self.assertEqual(upload_image("test_images.jpeg"), "https://storage.googleapis.com/smart-parking-21e9b.appspot.com/images/test_image.jpeg", "Correct")
      
if __name__ == '__main__':
   unittest.main()