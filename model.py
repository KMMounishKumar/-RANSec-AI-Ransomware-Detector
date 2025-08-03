# model.py

import os
import numpy as np
import joblib
import logging
from sklearn.ensemble import IsolationForest

# Create required folders
os.makedirs("model", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Setup logging
logging.basicConfig(
    filename="logs/model.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

MODEL_PATH = "model/rans_model.pkl"

def generate_dummy_data(n_samples=100):
    """
    Generates synthetic data representing normal and ransomware-like behavior.
    """
    try:
        np.random.seed(42)
        normal_data = np.random.normal(loc=0.3, scale=0.1, size=(n_samples, 4))
        ransomware_data = np.random.normal(loc=0.9, scale=0.05, size=(int(n_samples * 0.2), 4))
        data = np.vstack((normal_data, ransomware_data))
        np.random.shuffle(data)
        logging.info("[DATA] Dummy data generated successfully.")
        return data
    except Exception as e:
        logging.error(f"[DATA ERROR] Failed to generate data: {e}")
        return np.empty((0, 4))

def train_model():
    """
    Trains and saves the Isolation Forest model.
    """
    try:
        data = generate_dummy_data()
        if data.size == 0:
            raise ValueError("No data available for training.")

        model = IsolationForest(contamination=0.2, random_state=42)
        model.fit(data)
        joblib.dump(model, MODEL_PATH)
        logging.info("[MODEL] Isolation Forest trained and saved at %s", MODEL_PATH)
    except Exception as e:
        logging.error(f"[TRAINING ERROR] {e}")

def predict(input_features):
    """
    Predicts if the input is ransomware (-1) or normal (1).
    """
    try:
        if not os.path.exists(MODEL_PATH):
            logging.warning("[MODEL] Model not found. Training now...")
            train_model()
        model = joblib.load(MODEL_PATH)
        score = model.decision_function([input_features])[0]
        prediction = model.predict([input_features])[0]
        logging.info(f"[PREDICT] Input: {input_features} | Score: {score:.4f} | Result: {'Ransomware' if prediction == -1 else 'Normal'}")
        return prediction, score
    except Exception as e:
        logging.error(f"[PREDICTION ERROR] {e}")
        return 1, 0.0  # Default to normal

if __name__ == "__main__":
    train_model()
    # Example usage
    test_input = [0.92, 0.85, 0.78, 0.88]
    pred, score = predict(test_input)
    print(f"Prediction: {'Ransomware' if pred == -1 else 'Normal'}, Score: {score:.4f}")