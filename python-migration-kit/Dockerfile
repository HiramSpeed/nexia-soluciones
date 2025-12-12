# 🐳 Dockerfile Template for Python Apps
# Compatible with Hostinger VPS / Easypanel

# 1. Base Image: Lightweight Python
FROM python:3.10-slim

# 2. Set Environment Variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# 3. Create and set working directory
WORKDIR /app

# 4. Install System Dependencies (Optional, uncomment if needed for DB drivers like Postgres)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 5. Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy Project Code
COPY . .

# 7. Expose Port (Standard for Gunicorn/Uvicorn)
EXPOSE 8000

# 8. Start Command (Uncomment the one matching your framework)

# 👉 Option A: Flask (using Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

# 👉 Option B: Django (using Gunicorn)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

# 👉 Option C: FastAPI (using Uvicorn)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
