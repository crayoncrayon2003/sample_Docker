FROM python:3.10.14-slim

# Install curl for health check
RUN apt-get update && apt-get install -y curl && apt-get clean

# Set root directory
WORKDIR /app

# Copy files from local to container
COPY app/ .

# Install modules
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make the port public
EXPOSE 8000

# Launch the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
