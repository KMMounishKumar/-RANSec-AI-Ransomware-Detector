
from watchdog.events import FileSystemEventHandler

class RansomwareFileMonitor(FileSystemEventHandler):
    def on_created(self, event):
        print(f"[Monitor] File created: {event.src_path}")

    def on_modified(self, event):
        print(f"[Monitor] File modified: {event.src_path}")
