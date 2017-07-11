FROM python:3-alpine

ENV REDIS_URL="redis://redis:6379" \
    DJANGO_SETTINGS_MODULE="settings"

ADD ./ /opt/otree

RUN apk -U add --no-cache bash \
                          curl \
                          gcc \
                          musl-dev \
                          postgresql \
                          postgresql-dev \
    && pip install --no-cache-dir -r /opt/otree/requirements.txt \
    && curl https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz \
    | tar -xz -C /usr/local/bin \
    && mkdir -p /opt/init \
    && chmod +x /opt/otree/entrypoint.sh \
    && apk del curl gcc musl-dev postgresql-dev \
    && echo "oTree: /bin/bash -c 'cd /opt/otree && otree runprodserver --port=80'"> /Procfile

WORKDIR /opt/otree
VOLUME /opt/init
ENTRYPOINT /opt/otree/entrypoint.sh
EXPOSE 80
