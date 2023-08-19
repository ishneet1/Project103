import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = '< Set path for tracking file system events>'
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted!")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved!")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")

    #Initialize Event Handler Class

    #Initialize Observer

    #Schedule the Observer

    #Start the Observer

try:
    while True:
        time.sleep(2)
        print('running...')
except KeyboardInterrupt:
    print('stopped!')
    Observer.stop()
