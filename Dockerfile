FROM python:3.11.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    gcc \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo '#!/bin/bash\npython health_check.py & python main.py' > start.sh
RUN chmod +x start.sh
EXPOSE 8000

CMD ["./start.sh"]
