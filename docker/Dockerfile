FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Define environment variables
ENV PYTHONUNBUFFERED="1" \
    PYTHONIOENCODING="UTF-8" \
    LANG="C.UTF-8" \
    PYTHONPATH="/app:$PYTHONPATH" \
    FALCON_NUM_WORKERS=2 \
    FALCON_WORKER_TIMEOUT=60 \
    LOG_FILENAME="/dev/stdout"

# Add all locales
RUN apt-get clean && apt-get update && apt-get install -y locales \
    && sed -i '/nb_\|en_\|sv_\|se_/s/^#//g' /etc/locale.gen \
    && cat /etc/locale.gen \
    && locale-gen

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN apt-get update && \
    apt-get install build-essential libcurl4-openssl-dev \
    libssl-dev mime-support libpcre3 libpcre3-dev -y && \
    pip install --trusted-host pypi.python.org gunicorn

# Copy requirements.txt before rest of repo for caching
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run application when the container launches
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["gunicorn"]
