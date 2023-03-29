#!/usr/bin/env bash

set -e

if [ "$1" = 'gunicorn' ]; then
    # Falcon support
    if cat requirements.txt | grep -q -i falcon && [ -z "$FALCON_MODULE" ]; then
        FALCON_MODULE=application:app
    fi

    # Gunicorn default, if envvar $PORT is defined, is to bind to 0.0.0.0:$PORT
    # if only port provided to -b, 0.0.0.0 is assumed, like in uwsgi
    exec gunicorn $FALCON_MODULE -b 0.0.0.0:8080 -w $FALCON_NUM_WORKERS -t $FALCON_WORKER_TIMEOUT -k uvicorn.workers.UvicornWorker
else
    exec "$@"
fi
