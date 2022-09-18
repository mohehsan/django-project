FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt update -y
RUN apt install pdftk -y
RUN apt install --fix-missing -y
RUN apt update -y

RUN mkdir /app

RUN ls /app
WORKDIR /app

RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD .. /app/