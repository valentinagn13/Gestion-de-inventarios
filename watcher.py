import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Archivo modificado: {event.src_path}. Reiniciando...")
            os.execv(sys.executable, ['python'] + sys.argv)

def start_watcher():
    path = "."  # Monitorea el directorio actual
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)  # Mantiene el observador corriendo
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
