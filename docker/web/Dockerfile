# pull official base image
FROM python:3.12-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmemcached-dev zlib1g-dev libjpeg62-turbo-dev libffi-dev \
    libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libpq-dev

RUN pip install --upgrade pip
RUN pip --version
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
