# Use a lightweight Python image as the base (change version if needed)
FROM python:3.11

# Install uv
RUN pip install uv


# Update PATH to include uv installation directory
ENV PATH="$PATH:$HOME/.cargo/bin"
COPY requirements.txt .

RUN uv venv
# Install dependencies using uv pip
RUN uv pip install -r requirements.txt


# Install dependencies using uv pip
#RUN uv pip install --no-dev --no-interaction --no-ansi -r requirements.txt

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and requirements.txt
COPY . .

# Expose port 5000 for Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

