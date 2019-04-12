ARG FROM_TAG=3.6-slim
FROM python:$FROM_TAG

# Create the user and group first as they shouldn't change often.
# Specify the UID/GIDs so that they do not change somehow and mess with the
# ownership of external volumes.
RUN addgroup --system --gid 101 django \
    && adduser --system --uid 101 --ingroup django django \
    && mkdir /etc/gunicorn

# Install gosu so we can switch between users
RUN apt-get update && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/*

# Install Gunicorn
COPY gunicorn/ /etc/gunicorn/
RUN pip install --no-cache -r /etc/gunicorn/requirements.txt

WORKDIR /app

EXPOSE 8000

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
