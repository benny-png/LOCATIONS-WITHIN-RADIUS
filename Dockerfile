# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.2
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/bin/bash" \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container.
COPY . .

# Create the directory for the SQLite database
RUN mkdir -p /app/data && chown -R appuser:appuser /app/data

# Change ownership of the application directory to appuser
RUN chown -R appuser:appuser /app

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]