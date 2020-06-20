FROM python:3.8.3-slim-buster

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    gnupg \
 && git clone https://github.com/Seeed-Studio/grove.py \
 && pip install grove.py \
 && rm -rfv grove.py \
 && apt-get remove -y \
    git \
    gcc \
    gnupg \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY server.py /server.py

EXPOSE 80
ENTRYPOINT ["python", "server.py"]
