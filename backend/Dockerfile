# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install system dependencies (needed for pgvector/psycopg if binary wheels aren't used)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project definition
COPY pyproject.toml /code/

# Install dependencies
# We install directly from pyproject.toml
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

# Copy the rest of the application
COPY . /code/

# Make the entrypoint executable
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Create a non-root user for security
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Run the entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]