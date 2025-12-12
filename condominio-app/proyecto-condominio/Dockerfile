# 🐳 Dockerfile for Condominio App (Django)

# 1. Base Image
FROM python:3.10-slim

# 2. Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Work Directory
WORKDIR /app

# 4. Install Dependencies
COPY requirements.txt .
# Install packages. Note: We use --no-cache-dir to keep image small
# We might need to upgrade pip first
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Ensure gunicorn is installed (it was not in the original requirements.txt explicit list)
RUN pip install gunicorn

# 5. Copy Project Code
COPY . .

# 6. Static Files and Database Setup
# We create a directory for static files where collectstatic will put them
RUN mkdir -p staticfiles
RUN python manage.py collectstatic --noinput

# 7. Expose Port
EXPOSE 8000

# 8. Start Command
# Using gunicorn to serve config.wsgi
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
