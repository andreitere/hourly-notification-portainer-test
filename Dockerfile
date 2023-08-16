FROM python:3.9

RUN pip install requests apscheduler

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
