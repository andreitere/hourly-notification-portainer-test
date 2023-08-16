FROM python:3.9

RUN pip install requests

WORKDIR /app

ENV VERSION=2

COPY app.py .

CMD ["python", "app.py"]
