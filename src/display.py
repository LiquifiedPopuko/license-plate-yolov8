import cv2
import numpy as np
from enum import Enum
import time

img_path = './src/image/'

class Display(Enum):
    DENY = img_path+'deny.jpg'
    PASS = img_path+'pass.jpg'
    STANDBY = img_path+'standby.jpg'

state = Display.STANDBY
last_change = time.time()

def get_state(result):
    global state
    if result:
        print("set pass")
        state = Display.PASS
    else:
        print("set deny")
        state = Display.DENY

def set_access_image_state(result):
    global state, last_change
    last_change = time.time()
    get_state(result)

def get_state_image():
    global state, last_change
    if time.time() - last_change > 3:
        state = Display.STANDBY
        return cv2.imread(state.value)
    return cv2.imread(state.value)