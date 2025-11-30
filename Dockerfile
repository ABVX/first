FROM python:3.9-alpine
RUN pip install psutil
WORKDIR /app
COPY real_disk_monitor.py .
CMD ["python", "real_disk_monitor.py"]
