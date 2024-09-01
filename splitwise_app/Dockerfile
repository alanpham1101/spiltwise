FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wait-for-it.sh /code/

RUN chmod +x /code/wait-for-it.sh

COPY . /code/
