# sysntax=docker/dockerfile:1
# Filename: Dockerfile
# Description: Dockerfile for the Django application
FROM python:3.10-slim
USER root
WORKDIR /app

# Install system dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the source code
COPY . .

# Run the application
EXPOSE 8000
CMD ["python", "littlelemon/manage.py", "runserver", "0.0.0.0:8000"]

