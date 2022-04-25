# syntax=docker/dockerfile:1

# Tests image
FROM python:3.8-slim-buster

RUN apt update
RUN apt upgrade -y
RUN apt dist-upgrade
RUN apt-get install procps -y
RUN apt install curl -y
RUN apt install net-tools -y

WORKDIR /home/pos

COPY requirements.txt ./.

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src ./src

EXPOSE 8000

CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]
