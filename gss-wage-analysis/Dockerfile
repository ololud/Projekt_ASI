FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY pyproject.toml requirements.txt ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        gcc \
        libpq-dev \
        python3-dev \
        && pip install --upgrade pip \
        && pip install -r requirements.txt \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

COPY . .

COPY data/ data/

ENTRYPOINT ["kedro"]
CMD ["run"]
