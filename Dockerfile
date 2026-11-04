FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and data
COPY . .

# Ensure data directory and SQLite database are fully writable by Hugging Face user
RUN mkdir -p data && chmod -R 777 /app

# Hugging Face Spaces standard port is 7860
EXPOSE 7860

ENV HOST=0.0.0.0
ENV PORT=7860
ENV PYTHONUNBUFFERED=1

CMD ["python", "run.py"]
