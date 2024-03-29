FROM python:3.10-slim-buster
WORKDIR /app/
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .