from flask import Flask
import logging
import random
import time

app = Flask(__name__)

# Configure logging
#logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/")
def index():
    messages = [
        "User logged in successfully",
        "Database connection error",
        "Service is running fine",
        "Failed to fetch API response",
        "System memory usage high",
    ]
    log_message = random.choice(messages)
    
    if "error" in log_message.lower() or "failed" in log_message.lower():
        app.logger.error(log_message)
    else:
        app.logger.info(log_message)
    
    return log_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

