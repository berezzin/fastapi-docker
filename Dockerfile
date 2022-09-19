FROM python:3.10-slim-buster
WORKDIR /app/
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]