import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/vrish_fl8o8kc/Downloads"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hello, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops, {event.src_path} has been deleted!")
    def on_modified(self, event):
        print(f"Oops, {event.src_path} has been modified!")
    def on_moved(self,event):
        print(f"Oops, {event.src_path} has been moved or renamed!")
    
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive= True)
observer.start()

while True:
    time.sleep(2)
    print("walking...")








# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)#recursive looks for files inside files making sure every data is taken


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    