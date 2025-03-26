# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py test.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run tests on build (optional but recommended)
RUN pytest test.py

# Default command (interactive mode)
CMD ["python3"]

