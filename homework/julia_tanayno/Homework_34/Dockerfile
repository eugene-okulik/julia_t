FROM python
COPY docker_task.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "docker_task.py"]