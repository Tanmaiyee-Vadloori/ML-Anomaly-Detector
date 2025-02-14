# Log Anomaly Detection with Flask and Isolation Forest

## Overview
This project consists of a Flask application that generates log messages and a machine-learning script that detects anomalies in those logs using Isolation Forest. The solution can help identify unusual system behaviors, potential security threats, or operational issues based on log analysis.

## Project Structure
```
.
├── app.py          # Flask application to generate logs
├── logs.txt        # Log file storing generated logs
├── anomaly_detector.py  # Script for detecting anomalies in logs
├── Dockerfile      # Docker configuration to containerize the application
├── README.md       # Documentation file
```

## Features
- **Flask Application (`app.py`)**
  - Generates log messages with different severity levels (INFO, WARNING, ERROR).
  - Logs messages to `logs.txt`.
  - Accessible via a web browser on `http://localhost:5000/`.

- **Anomaly Detection (`anomaly_detector.py`)**
  - Loads logs from `logs.txt`.
  - Extracts log messages for processing.
  - Vectorizes log messages into numerical features.
  - Trains an Isolation Forest model for anomaly detection.
  - Detects and flags unusual log messages as anomalies.

- **Docker Support**
  - The `Dockerfile` allows easy containerization and deployment of the Flask application.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- pip
- Docker (optional, for containerized deployment)

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Running the Flask Application
Start the Flask application to generate logs:
```sh
python app.py
```
Access the application at `http://localhost:5000/`, and it will randomly log messages in `logs.txt`.

### Running the Anomaly Detection Script
Once logs are generated, run the anomaly detection script:
```sh
python anomaly_detector.py
```
It will process the logs and display any detected anomalies.

### Running with Docker
To build and run the Flask app inside a Docker container:
```sh
docker build -t log-analyzer .
docker run -p 5000:5000 log-analyzer
```

## Example Output
After running `anomaly_detector.py`, you may see output like:
```
🚀 Running anomaly detection on new logs...
⚠️ Anomalies detected!
🔴 Database connection failed
🔴 Unauthorized admin access attempt detected
```
If no anomalies are detected, it will output:
```
✅ No anomalies detected.
```

## Customization
- Modify `logs.txt` with additional log data.
- Adjust `contamination=0.2` in `anomaly_detector.py` to fine-tune anomaly sensitivity.
- Extend the Flask application to integrate with external log sources.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.


