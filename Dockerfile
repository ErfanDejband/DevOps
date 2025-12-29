FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements-dev.txt ./

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY src/ ./src/
COPY tests/ ./tests/

ENV PYTHONPATH=/app

CMD ["python", "-c", "from src.temperature_api import TemperatureSensor; print('Temperature API Ready!')"]