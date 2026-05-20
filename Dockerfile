# Stage 1: Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app_new.py .
COPY linkedin_extension/ ./linkedin_extension/

# Expose port
EXPOSE 9011

# Health check (optional but recommended)
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:9011/docs')" || exit 1

# Run the FastAPI application
CMD ["uvicorn", "app_new:app", "--host", "0.0.0.0", "--port", "9011"]
