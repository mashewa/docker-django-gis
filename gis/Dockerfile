FROM python:3.9-alpine3.17
LABEL maintainer="royalwagon.ca"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./server /server
WORKDIR /server
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    apk add --update --no-cache geos proj gdal binutils && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf \tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

USER django-user

