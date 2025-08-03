import os
import logging
import shutil
from datetime import datetime

# Ensure required folders exist
os.makedirs('logs', exist_ok=True)
os.makedirs('quarantine', exist_ok=True)

# Configure logging
log_file = 'logs/response.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def quarantine_file(file_path):
    """
    Moves the specified file to a quarantine directory with a timestamp.
    """
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found or already moved.")

        filename = os.path.basename(file_path)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_name = f"{timestamp}_{filename}"
        target_path = os.path.join('quarantine', new_name)

        shutil.move(file_path, target_path)
        logging.info(f"[QUARANTINE] File moved to quarantine: {file_path} → {target_path}")
    except Exception as e:
        logging.error(f"[ERROR] Failed to quarantine file: {file_path} - {e}")

def kill_process(pid):
    """
    Attempts to kill the process with the given PID.
    """
    try:
        if not isinstance(pid, int) or pid <= 0:
            raise ValueError("Invalid PID")
        os.kill(pid, 9)
        logging.info(f"[KILL] Process terminated: PID {pid}")
    except Exception as e:
        logging.error(f"[ERROR] Failed to kill process {pid} - {e}")

def send_alert(message):
    """
    Logs and prints a security alert message.
    """
    alert_msg = f"[ALERT] {message}"
    logging.warning(alert_msg)
    print(alert_msg)

# Example test usage
if __name__ == '__main__':
    send_alert("Suspicious activity detected: High anomaly score.")
    # Replace with actual file path and PID when testing
    quarantine_file("test_data/ransom_note.txt")
    kill_process(12345)
