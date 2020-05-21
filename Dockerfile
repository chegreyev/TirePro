FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8

COPY ./src /src
WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install pipenv && pipenv install --deploy --system

