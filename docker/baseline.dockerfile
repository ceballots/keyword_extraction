#Dockerfile for notebooks
FROM python:3.8.0-slim
WORKDIR /app

COPY requirements.txt /app

# `pip cache list` spits out cache contents -- doesn't impact functionality but shows that the cache is working.
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip3 install -r requirements.txt

COPY . /app
