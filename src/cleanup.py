import os, shutil

file_path = '/home/orangepi/.pyenv/runs/detect/'

def cleanup():
    for x in os.listdir(file_path):
        if x.startswith('predict'):
            shutil.rmtree(file_path+x)