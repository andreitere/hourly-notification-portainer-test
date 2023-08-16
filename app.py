import os
import time
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def send_notification(topic):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Current time: {current_time}\nHave a great day!"

    url = f"https://ntfy.sh/{topic}"
    payload = message.encode(encoding='utf-8')

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print("Failed to send notification.")

def health_log():
    print("Service is running...")

def main():
    topic = os.getenv("NOTIFY_TOPIC")

    if not topic:
        print("NOTIFY_TOPIC environment variable is not set. Notification will not be sent.")
        return

    scheduler = BlockingScheduler()
    # Schedule the job using a cron expression (e.g., every hour)
    scheduler.add_job(send_notification, 'cron', args=[topic], hour='*')
    scheduler.add_job(health_log, 'interval', args=[], minutes=5)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
