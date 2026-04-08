from datetime import datetime
import uuid

class Logger:
    def __init__(self, file="error_log.txt"):
        self.file = file

    def log(self, message):
        unique_id = uuid.uuid4()
        log_message = f"{unique_id} | {datetime.now()} | {message}"

        with open(self.file, "a") as f:
            f.write(log_message + "\n")

        print("Logged:", log_message)
        # Added for commit history screenshot

