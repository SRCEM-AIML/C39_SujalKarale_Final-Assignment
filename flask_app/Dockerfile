FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first to utilize Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose Flask default port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
