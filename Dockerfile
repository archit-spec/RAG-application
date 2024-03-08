# Use a lightweight Python image as the base
FROM python:3.9-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependency files necessary for installing dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

