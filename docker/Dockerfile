# environment to build the README.md document from dataframe.csv
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pandas && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
CMD ["python3"]