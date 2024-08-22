FROM python:latest
COPY . /app
CMD ["python", "./app/main/main.py"]