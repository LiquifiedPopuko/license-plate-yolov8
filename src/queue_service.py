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

# this function check if the thread is alive before adding new queue
def add_queue(load):
   if queue_worker.is_alive():
      print("Add queue")
      q.put(load)
   else:
      print("Refresh/respawn thread")
      queue_worker.start()

# Turn-on the worker thread.
queue_worker = Thread(target=license_access_worker, daemon=True)

# Block until all tasks are done.
q.join()
print('All work completed, close thread')
queue_worker.is_alive()