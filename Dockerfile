FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Securitate 2026: Rulăm ca utilizator non-root
RUN useradd -m adrian_ops
USER adrian_ops

CMD ["python", "monitoring/health_monitor.py"]




