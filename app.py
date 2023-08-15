import os
import time
import requests
from datetime import datetime

topic = os.getenv("NOTIFY_TOPIC")

if topic:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Current time: {current_time}\nHave a great day!"

        url = f"https://ntfy.sh/{topic}"
        payload = message.encode(encoding='utf-8')

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print("Failed to send notification.")

        time.sleep(60)  # Sleep for an hour
else:
    print("NOTIFY_TOPIC environment variable is not set. Notification will not be sent.")
