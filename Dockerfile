FROM python:3.7-alpine
MAINTAINER rocketsiran

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /usr/src/app
COPY . ./

RUN adduser -D user
USER user
