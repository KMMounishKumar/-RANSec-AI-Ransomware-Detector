# -RANSec-AI-Ransomware-Detector


#  RANSec – AI-Powered Ransomware Detection System

RANSec is an intelligent, real-time ransomware detection system designed to monitor file behavior and respond to suspicious activity using machine learning. Built as part of my ML internship and personal exploration into AI-based cybersecurity, this project combines data science, real-time monitoring, and automation.

##  Features

-  Monitors system directories for suspicious file operations
-  Detects ransomware using trained ML models (Random Forest, Isolation Forest)
-  Real-time alerts, file quarantine, and automatic system response
-  Interactive Flask dashboard for live logs and status
-  Designed to run in the background at system startup
-  Deployment-ready (Docker + Cloud integration)

##  ML Techniques Used

- **Feature extraction** from file behavior logs
- **Supervised & unsupervised learning** for anomaly detection
- **Model evaluation** using precision, recall, and F1-score
- **Live inference pipeline** integrated with the system monitor




## 📂 Project Structure

```bash
├── model.py               # ML training + prediction logic
├── monitor.py             # Monitors file changes
├── responder.py           # Quarantine and alert system
├── dashboard.py           # Flask app for live updates
├── simulate_ransomware.py # Fake attack to test the system
├── run_all.py             # Launches all components
└── main.py                # Main launcher script
└── ransomware.py          # Ransomware simulator for testing detection
└── README.md              # This file

