FROM python:3.10-slim

WORKDIR /app

# Install required tools
RUN apt-get update && apt-get install -y \
    tcpdump libpcap-dev iproute2 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Run the inquisitor program
CMD ["python", "inquisitor.py"]
