FROM ubuntu:22.04

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python3","app.py"]
