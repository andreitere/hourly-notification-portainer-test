FROM python:3.9


RUN apt-get update && apt-get install -y tzdata
ENV TZ=Europe/Bucharest
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install requests apscheduler

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
