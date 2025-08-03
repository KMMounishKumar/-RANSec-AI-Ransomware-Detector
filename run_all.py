import os
import subprocess
import threading
import time
import webbrowser

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXEC = "/Users/mounishkumarkm/.pyenv/versions/proj2_3.10_env/bin/python"
DASHBOARD_SCRIPT = os.path.join(BASE_DIR, "dashboard.py")
MAIN_SCRIPT = os.path.join(BASE_DIR, "main.py")

# Launch Flask dashboard in background
def launch_dashboard():
    print("[RANSec] Launching dashboard...")
    subprocess.Popen([PYTHON_EXEC, DASHBOARD_SCRIPT])
    time.sleep(3)  # Give the server time to start
    webbrowser.open("http://127.0.0.1:5000")

# Launch monitor in main thread
def launch_monitor():
    print("[RANSec] Launching monitor...")
    subprocess.run([PYTHON_EXEC, MAIN_SCRIPT])

if __name__ == "__main__":
    dashboard_thread = threading.Thread(target=launch_dashboard)
    dashboard_thread.start()

    launch_monitor()