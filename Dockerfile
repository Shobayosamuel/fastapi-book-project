# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Update package lists and install NGINX
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for your app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Copy the NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port (Heroku will override $PORT)
EXPOSE $PORT

# Start NGINX and Gunicorn
CMD bash -c "gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000 --workers 4 & nginx -g 'daemon off;'"