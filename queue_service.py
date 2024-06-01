from queue import Queue
from threading import Thread
import requests
import time
import logging

logger = logging.getLogger("response")
logging.basicConfig(filename='response.log', encoding='utf-8', level=logging.INFO)

url = "http://13.214.18.38:8000/api/addHistory"
num_fetch_threads = 1
q = Queue()

def license_access_worker():
   while True:
      load = q.get()
      print("Sending POST request of:"+str(load))
      response = requests.post(url=url, json=load)
      print(response)
      if not response.ok:
         logging.info('Unsucessful load: %s', load)
      else:
         logging.info('Successful load: %s', load)
      q.task_done()

# Turn-on the worker thread.
Thread(target=license_access_worker, daemon=True).start()

# Send thirty task requests to the worker.
q.put({
   "license_id": 60,
   "access_date": "2024-06-20 18:45:54",
   "access_type": 2,
   "image_source": "https://storage.googleapis.com/smart-parking-21e9b.appspot.com/images/%E0%B8%82%E0%B8%97%209515_20240531T205019.jpg"
})

# Block until all tasks are done.
q.join()
print('All work completed')