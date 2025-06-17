FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt dependencies_installer.py .
RUN python dependencies_installer.py

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]