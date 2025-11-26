# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies (optional but useful for many Python libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better Docker caching)
COPY requirements-prod.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy the rest of the project into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to start the FastAPI app using Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
