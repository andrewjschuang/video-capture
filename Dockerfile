FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=0

ENV FLASK_APP=server.py

CMD ["flask", "run", "--host", "0.0.0.0"]
