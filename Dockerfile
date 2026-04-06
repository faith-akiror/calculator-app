# Use official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run tests to make sure container is healthy
RUN pytest && behave

# Default command (change to your app command if needed)
CMD ["python", "-c", "print('Calculator app container is ready!')"]