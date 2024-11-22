# Use Python 3.9 slim image
FROM python:3.9-slim

# Install system dependencies
<<<<<<< HEAD
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && apt-get clean \
=======
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
>>>>>>> ffd15aea85fc1753f84bab6f1ea0050ac280c39d
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

<<<<<<< HEAD
# Copy requirements file and install dependencies
=======
# Copy requirements first (for better caching)
>>>>>>> ffd15aea85fc1753f84bab6f1ea0050ac280c39d
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

<<<<<<< HEAD
# Create necessary directories
=======
# Make sure the templates directory exists
>>>>>>> ffd15aea85fc1753f84bab6f1ea0050ac280c39d
RUN mkdir -p templates

# Set environment variables
ENV PORT=8080
<<<<<<< HEAD
ENV PYTHONUNBUFFERED=1


EXPOSE 8080

# Use JSON array syntax for CMD to ensure proper signal handling
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "app:app"]
=======

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
>>>>>>> ffd15aea85fc1753f84bab6f1ea0050ac280c39d
