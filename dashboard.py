import os
import logging
from flask import Flask, render_template_string
from responder import send_alert
import webbrowser
webbrowser.open("http://127.0.0.1:5000")
app = Flask(__name__)

# Ensure folders exist
os.makedirs('logs', exist_ok=True)
os.makedirs('quarantine', exist_ok=True)

# Logging setup
log_file = 'logs/dashboard.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.route('/')
def dashboard():
    # Load last 10 log entries
    try:
        with open('logs/response.log', 'r') as f:
            logs = f.readlines()[-10:]
    except FileNotFoundError:
        logs = ["No logs available."]

    # Load quarantined file names
    try:
        quarantined_files = os.listdir('quarantine')
        quarantined_files = sorted(quarantined_files, reverse=True)[:10]
    except FileNotFoundError:
        quarantined_files = []

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>RANSec Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; background: #111; color: #eee; text-align: center; padding: 40px; }
            .card { background: #222; padding: 20px; margin: auto; width: 70%; border-radius: 10px; box-shadow: 0 0 10px #444; margin-bottom: 20px; }
            h1 { color: #FF4F4F; }
            h2 { color: #79D1C3; }
            pre { text-align: left; background: #333; padding: 10px; border-radius: 5px; overflow-x: auto; }
            ul { text-align: left; padding-left: 30px; }
            li { margin-bottom: 5px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔒 RANSec Dashboard</h1>
            <p>Status: <strong style="color: #4CAF50;">Monitoring Active</strong></p>
            <p>Logs: <code>logs/response.log</code> | Quarantine: <code>quarantine/</code></p>
        </div>

        <div class="card">
            <h2>📄 Recent Log Entries</h2>
            <pre>{{ logs }}</pre>
        </div>

        <div class="card">
            <h2>📦 Quarantined Files</h2>
            {% if files %}
                <ul>
                {% for f in files %}
                    <li>{{ f }}</li>
                {% endfor %}
                </ul>
            {% else %}
                <p>No files quarantined yet.</p>
            {% endif %}
        </div>
    </body>
    </html>
    """, logs="".join(logs), files=quarantined_files)

if __name__ == '__main__':
    send_alert("Test alert from RANSec dashboard.")
    app.run(host='127.0.0.1', port=5000, debug=True)