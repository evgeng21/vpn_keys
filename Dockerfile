FROM python:3.11-alpine

COPY src/requirements.txt ./requirements.txt
COPY ./src /src
WORKDIR .
EXPOSE 8010

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r requirements.txt

RUN adduser --disabled-password service-user

USER service-user