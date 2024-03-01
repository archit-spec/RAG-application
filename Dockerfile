# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install necessary dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libopenblas-dev \
        liblapack-dev \
        libomp-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the Flask application code into the container
COPY . .

# Expose port 5000 for Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

