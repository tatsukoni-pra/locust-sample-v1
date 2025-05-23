FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y \
  build-essential && \
  pip install --upgrade pip \
  locust lxml && \
  echo `python --version` && \
  locust -V

WORKDIR /app/src
