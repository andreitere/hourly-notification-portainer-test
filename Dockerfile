FROM python:3.9

RUN pip install requests

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
