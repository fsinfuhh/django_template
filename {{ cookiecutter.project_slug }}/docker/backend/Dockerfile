FROM python:3.11-slim

# Install normal dependencies
RUN apt-get update && apt-get -y --no-install-recommends install build-essential nginx && rm -rf /var/lib/apt/lists/*

# Add project code to container
VOLUME /app/backend
WORKDIR /app/backend

# Install Python dependencies
RUN pip3 install pipenv==v2022.4.20

RUN usermod -u 2009 -g 33 -d /app/backend www-data

ADD ./docker/backend/env.dev.local /app/config/.env.dev.local

EXPOSE 8000

#USER www-data:www-data
ADD ./docker/backend/start.sh /usr/local/bin/start.sh
CMD ["bash", "/usr/local/bin/start.sh"]
