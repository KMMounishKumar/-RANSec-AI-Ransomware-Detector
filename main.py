import time
import logging
import os
from watchdog.observers import Observer
from file_monitor import RansomwareFileMonitor
from model import predict
from responder import quarantine_file, kill_process, send_alert

# Path to monitor
WATCH_PATH = os.path.expanduser("~/Downloads")

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Enhanced feature extractor
def extract_features(file_path):
    # TODO: add real feature extraction
    return [0.92, 0.85, 0.78, 0.88]

# Custom event handler
class RANSecHandler(RansomwareFileMonitor):
    def on_created(self, event):
        super().on_created(event)
        if not event.is_directory:
            self.handle_file(event.src_path)

    def on_modified(self, event):
        super().on_modified(event)
        if not event.is_directory:
            self.handle_file(event.src_path)

    def handle_file(self, file_path):
        features = extract_features(file_path)
        prediction, score = predict(features)
        if prediction == -1:
            send_alert(f"🚨 Ransomware detected: {file_path} | Score: {score:.4f}")
            quarantine_file(file_path)
            kill_process(99999)  # Dummy placeholder

# Start monitoring
def start_watchdog():
    print(f"[RANSec] Live monitoring: {WATCH_PATH}")
    handler = RANSecHandler()
    observer = Observer()
    observer.schedule(handler, WATCH_PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    start_watchdog()