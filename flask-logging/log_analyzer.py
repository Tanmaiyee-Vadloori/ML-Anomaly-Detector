import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

# Load logs
def load_logs(file_path="logs.txt"):
    try:
        with open(file_path, "r") as file:
            logs = [line.strip() for line in file.readlines() if line.strip()]
            if not logs:
                print("Error: No logs found!")
                exit(1)
            print("Loaded Logs:", logs)  # Debugging print
            return logs
    except FileNotFoundError:
        print(f"Error: Log file '{file_path}' not found.")
        exit(1)

# Extract message from log lines
def extract_log_messages(logs):
    log_messages = []
    for log in logs:
        match = re.search(r"(?:INFO|ERROR|WARNING):\s*(.*)", log)
        if match:
            log_messages.append(match.group(1))
    return log_messages if log_messages else logs  # Ensure non-empty return

# Convert log messages to numerical data
def vectorize_logs(log_messages):
    print("Received Logs for Vectorization:", log_messages)  # Debugging print
    if not log_messages:
        print("Error: No logs to process!")
        exit(1)
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(log_messages)
    
    if X.shape[1] == 0:
        print("Error: No valid words found in logs for vectorization!")
        exit(1)
    
    return X, vectorizer

# Train Isolation Forest Model
def train_model(features):
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(features)
    return model

# Detect anomalies
def detect_anomalies(model, vectorizer, new_logs):
    if not new_logs:
        return []
    
    transformed_logs = vectorizer.transform(new_logs)
    predictions = model.predict(transformed_logs)
    anomalies = [new_logs[i] for i, p in enumerate(predictions) if p == -1]
    return anomalies

# Main execution
if __name__ == "__main__":
    logs = load_logs()
    log_messages = extract_log_messages(logs)
    
    features, vectorizer = vectorize_logs(log_messages)
    model = train_model(features)

    # Simulate real-time detection
    print("\U0001F680 Running anomaly detection on new logs...")
    anomalies = detect_anomalies(model, vectorizer, log_messages)

    if anomalies:
        print("\u26A0\uFE0F Anomalies detected!")
        for anomaly in anomalies:
            print(f"\U0001F534 {anomaly}")
    else:
        print("\u2705 No anomalies detected.")
